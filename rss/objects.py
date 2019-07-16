from telegram import Bot
from telegram.utils.request import Request

from main_config import BotConfig

bot = Bot(token=BotConfig.token,
          base_url=BotConfig.base_url,
          request=Request(con_pool_size=BotConfig.connection_pool_size),
          base_file_url=BotConfig.base_file_url)
