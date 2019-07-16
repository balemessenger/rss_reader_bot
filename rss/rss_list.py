#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from telegram.ext import *

from DB.db_handler import get_rss_by_admin_chat_id
from constants.messages import BotMessage, Keyboards
from rss.default import start

logger = logging.getLogger()


def get_rss_list(bot, update):
    user = update.message.from_user
    rss_list = get_rss_by_admin_chat_id(user.id)
    if rss_list:
        text = "*لیست فیدخوان های شما* \n"
        for rss in rss_list:
            text += "کانال: {} // فیدخوان: {}\n\n".format(rss.channel_user_name, rss.rss_url)
        update.message.reply_text(text)
        start(bot, update)
        return ConversationHandler.END
    else:
        update.message.reply_text(BotMessage.no_rss)
        start(bot, update)
        return ConversationHandler.END


get_rss_list_handler = RegexHandler(pattern='^(' + Keyboards.get_rss_list + ')$', callback=get_rss_list)
