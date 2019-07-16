#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import *

from DB.db_handler import get_rss_by_admin_chat_id, remove_rss
from constants.messages import BotMessage, ConversationStates, Keyboards
from rss.cancel import cancel
from rss.default import start

logger = logging.getLogger()


def select_rss(bot, update, user_data):
    user = update.message.from_user
    rss_list = get_rss_by_admin_chat_id(user.id)
    if rss_list:
        user_data["rss_list"] = rss_list
        buttons = []
        for rss in rss_list:
            buttons.append(rss.rss_url + rss.channel_user_name)
        reply_keyboard = [[Keyboards.back_to_main] + buttons]
        reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
        update.message.reply_text(BotMessage.select_rss, reply_markup=reply_markup)
        return ConversationStates.RSS
    else:
        update.message.reply_text(BotMessage.no_rss)
        start(bot, update)
        return ConversationHandler.END


def remove(bot, update, user_data):
    user = update.message.from_user

    input_text = update.message.text
    rss_list = user_data["rss_list"]

    for rss in rss_list:
        if rss.admin_chat_id == str(user.id) and rss.rss_url + rss.channel_user_name == input_text:
            remove_rss(rss)
    update.message.reply_text(BotMessage.remove_success)
    start(bot, update)
    return ConversationHandler.END


remove_rss_handler = RegexHandler(pattern='^(' + Keyboards.remove_rss + ')$', callback=select_rss, pass_user_data=True)

remove_rss_conversation_handler = ConversationHandler(
    entry_points=[remove_rss_handler],
    states={
        ConversationStates.RSS: [MessageHandler(Filters.text, remove, pass_user_data=True)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
