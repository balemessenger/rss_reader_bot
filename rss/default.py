import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import RegexHandler, CommandHandler, ConversationHandler

from constants.messages import Keyboards, BotMessage

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()


def start(bot, update):
    reply_keyboard = [[Keyboards.create_rss, Keyboards.get_rss_list, Keyboards.remove_rss, Keyboards.guide]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessage.start, reply_markup=reply_markup)
    return ConversationHandler.END


def guide(bot, update):
    reply_keyboard = [[Keyboards.back_to_main]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessage.help, reply_markup=reply_markup)
    return ConversationHandler.END


def error(bot, update, error_ex):
    logger.error(error.__name__)
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"')


guide_message_handler = RegexHandler(pattern='^(' + Keyboards.guide + ')$', callback=guide)
start_message_handler = RegexHandler(pattern='^(' + Keyboards.start + ')$', callback=start)
back_message_handler = RegexHandler(pattern='^(' + Keyboards.back_to_main + ')$', callback=start)

start_command_handler = CommandHandler('start', start)
