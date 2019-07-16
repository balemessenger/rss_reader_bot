# /bin/bash/python/
import time
from urllib.parse import unquote
from telegram.error import (TelegramError, Unauthorized)
from telegram import ParseMode
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread as RunningThread
import datetime
import threading
import traceback
from time import sleep

from DB.db_handler import get_all_rss, update_last_check, de_active_channel
from main_config import BotConfig
from rss.datehandler import DateHandler
from rss.feedhandler import FeedHandler


class BatchProcess(threading.Thread):

    def __init__(self, bot):
        RunningThread.__init__(self)
        self.update_interval = float(BotConfig.rss_interval)
        self.bot = bot
        self.running = True

    def run(self):
        """
        Starts the BatchThreadPool
        """

        while self.running:
            # Init workload queue, add queue to ThreadPool
            rss_queue = get_all_rss()
            self.parse_parallel(rss_queue=rss_queue, threads=4)

            # Sleep for interval
            sleep(self.update_interval)

    def parse_parallel(self, rss_queue, threads):
        time_started = datetime.datetime.now()

        pool = ThreadPool(threads)
        pool.map(self.update_feed, rss_queue)
        pool.close()
        pool.join()

        time_ended = datetime.datetime.now()
        duration = time_ended - time_started
        print("Finished updating! Parsed " + str(len(rss_queue)) +
              " rss feeds in " + str(duration) + " !")

    def update_feed(self, rss):
        if rss.is_active:  # is_active
            try:
                for post in reversed(FeedHandler.parse_feed(rss.rss_url)):
                    self.send_newest_messages(rss=rss, post=post)
            except Exception as e:
                traceback.print_exc()
                print(e)
                # message = "مشکلی در پردازش rss شما پیش آمده است!"
                de_active_channel(rss)
                # self.bot.send_message(chat_id=rss.admin_chat_id, text=message, parse_mode=ParseMode.HTML)

    def send_newest_messages(self, rss, post):
        print(post.title)
        post_update_date = DateHandler.parse_datetime(datetime=post.updated)
        post_update_date_timestamp = post_update_date.timestamp()
        url_update_date_timestamp = rss.last_updated

        print("====>", post_update_date_timestamp, type(post_update_date), " > ", url_update_date_timestamp,
              type(url_update_date_timestamp))
        print("2 ====>", post_update_date_timestamp > url_update_date_timestamp)

        if post_update_date_timestamp > url_update_date_timestamp:
            print("3 ====>", "reach")
            link = unquote(post.link)
            message = "*" + post.title + "*\n\n" + link
            try:
                print("4 ====>", "send message to ", rss.channel_chat_id, message)
                self.bot.send_message(chat_id=rss.channel_chat_id, text=message)
                time.sleep(0.5)
                print("5 ====>", "sent")
                update_last_check(rss=rss, last_updated=post_update_date_timestamp)

            except Unauthorized:
                de_active_channel(rss=rss)
            except TelegramError:
                pass

    def set_running(self, running):
        self.running = running
