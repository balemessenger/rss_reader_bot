import logging

from telegram.ext import ConversationHandler

logger = logging.getLogger()


def cancel(bot, update):
    logger.warning(cancel.__name__)
    update.message.reply_text('خداحافظ! متشکر از شما.')
    return ConversationHandler.END
