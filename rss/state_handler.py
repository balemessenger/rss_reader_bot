from rss.objects import bot
from rss.create_rss import *
from main_config import BotConfig
from rss.default import error, start_command_handler, start_message_handler, guide_message_handler, back_message_handler
from rss.remove_rss import remove_rss_conversation_handler
from rss.rss_list import get_rss_list_handler
# from rss.rss_send import BatchProcess
from rss.rss_send import BatchProcess


def main():
    updater = Updater(bot=bot)
    dp = updater.dispatcher
    dp.add_handler(start_message_handler)
    dp.add_handler(start_command_handler)
    dp.add_handler(get_rss_list_handler)
    dp.add_handler(guide_message_handler)
    dp.add_handler(back_message_handler)
    dp.add_handler(create_rss_conversation_handler)
    dp.add_handler(remove_rss_conversation_handler)
    dp.add_error_handler(error)
    processing = BatchProcess(bot=bot)
    processing.start()
    updater.start_polling(poll_interval=BotConfig.poll_interval)
    updater.idle()
