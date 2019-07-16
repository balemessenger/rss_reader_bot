#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import re

from telegram import ReplyKeyboardMarkup
from telegram.ext import *

from DB.db_handler import add_rss, get_rss_by_admin_chat_id
from DB.models.rss import RSS
from api.is_admin import is_admin
from constants.messages import BotMessage, ConversationStates, Keyboards
from rss.cancel import cancel
from rss.default import start

logger = logging.getLogger()


def create_rss(bot, update):
    user = update.message.from_user
    rss_list = get_rss_by_admin_chat_id(user.id)
    if rss_list:
        buttons = set()
        for rss in rss_list:
            buttons.add(rss.channel_user_name)
        reply_keyboard = [buttons]
        reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
        update.message.reply_text(BotMessage.enter_channel_id, reply_markup=reply_markup)
    else:
        update.message.reply_text(BotMessage.enter_channel_id)
    return ConversationStates.NICK_NAME


def check_is_admin(bot, update, user_data):
    user = update.message.from_user
    input_message = update.message.text
    pattern = re.compile("@([A-Za-z0-9_]+)")
    if not pattern.match(input_message):
        update.message.reply_text(BotMessage.invalid_username)
        start(bot, update)
        return ConversationHandler.END
    if is_admin(user.id, input_message):
        channel_user_name = input_message
        user_data["channel_user_name"] = channel_user_name
        channel_chat = bot.get_chat(channel_user_name)
        user_data["channel_chat_id"] = channel_chat.id
        update.message.reply_text(BotMessage.enter_rss_url)
        return ConversationStates.RSS
    else:
        update.message.reply_text(BotMessage.not_permitted)
        return ConversationHandler.END


def get_rss_and_add_it(bot, update, user_data):
    rss_url = update.message.text
    admin = update.message.from_user
    channel_user_name = user_data["channel_user_name"]
    channel_chat_id = user_data["channel_chat_id"]
    rss = RSS(channel_chat_id, channel_user_name, admin_chat_id=admin.id,
              admin_user_name=admin.username, rss_url=rss_url, last_updated=float(0))
    add_rss(rss)
    update.message.reply_text(BotMessage.rss_added_successfully)
    start(bot, update)
    return ConversationHandler.END


create_rss_handler = RegexHandler(pattern='^(' + Keyboards.create_rss + ')$', callback=create_rss)

create_rss_conversation_handler = ConversationHandler(
    entry_points=[create_rss_handler],
    states={
        ConversationStates.NICK_NAME: [MessageHandler(Filters.text, check_is_admin, pass_user_data=True)],
        ConversationStates.RSS: [MessageHandler(Filters.text, get_rss_and_add_it, pass_user_data=True)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)
