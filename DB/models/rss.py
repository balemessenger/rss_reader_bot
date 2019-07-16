from sqlalchemy import Column, Integer, String, Boolean, BigInteger

from DB.models.base import Base


class RSS(Base):
    __tablename__ = "rss"
    id = Column(Integer, primary_key=True)
    channel_chat_id = Column(String)
    channel_user_name = Column(String)
    admin_chat_id = Column(String)
    admin_user_name = Column(String)
    rss_url = Column(String)
    last_updated = Column(BigInteger)
    is_active = Column(Boolean, default=True)

    def __init__(self, channel_chat_id, channel_user_name, admin_chat_id, admin_user_name, rss_url):
        self.channel_chat_id = str(channel_chat_id)
        self.channel_user_name = str(channel_user_name)
        self.admin_chat_id = str(admin_chat_id)
        self.admin_user_name = str(admin_user_name)
        self.rss_url = rss_url
