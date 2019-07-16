# /bin/bash/python/
import asyncio
import time
from urllib.parse import unquote

import feedparser
from telegram.error import (TelegramError, Unauthorized)
from threading import Thread as RunningThread
import threading
import traceback
from time import sleep
from dateutil import parser

from DB.db_handler import get_all_rss, update_last_check, de_active_channel, get_rss_by_id
from main_config import BotConfig
from rss.objects import bot
from utils.utils import un_healthy, healthy


def check_connection():
    try:
        bot.get_updates()
    except Exception as e:
        print(e)
        un_healthy()


def utc_to_int(utc_date):
    dt = parser.parse(utc_date)
    return int(dt.strftime("%Y%m%d%H%M%S"))


class BatchProcess(threading.Thread):

    def __init__(self, bot):
        RunningThread.__init__(self)
        self.rss_interval = BotConfig.rss_interval
        self.bot = bot
        self.running = True
        self.loop = asyncio.get_event_loop()

    def run(self):
        """
        Starts the BatchThreadPool
        """

        while self.running:
            rss_queue = get_all_rss()
            for rss in rss_queue:
                self.update_feed(rss)
            print("Finished updating! Parsed " + str(len(rss_queue)) + " rss feeds")
            check_connection()
            sleep(self.rss_interval)

    def update_feed(self, rss):
        healthy()
        if rss.is_active:
            try:
                feed = feedparser.parse(rss.rss_url)
                entries = feed.entries
                entries = entries[::-1]
                for post in entries:
                    self.send_newest_messages(rss=rss, post=post)
            except Exception as e:
                traceback.print_exc()
                print(e)
                un_healthy()
                de_active_channel(rss)

    def send_newest_messages(self, rss, post):
        post_int_date = utc_to_int(post.published)
        if rss.last_updated is None:
            update_last_check(rss=rss, last_updated=post_int_date)
        rss = get_rss_by_id(rss.id)
        if post_int_date > rss.last_updated:
            link = unquote(post.link)
            message = str("*" + post.title + "*\n\n" + link)
            try:
                chat_id = rss.channel_chat_id
                self.bot.send_message(chat_id=chat_id, text=message)
                time.sleep(0.5)
                update_last_check(rss=rss, last_updated=post_int_date)
            except Unauthorized:
                de_active_channel(rss=rss)
            except TelegramError:
                pass
            except Exception as e:
                print(e)
                un_healthy()

    def set_running(self, running):
        self.running = running
