import logging
from DB.models.base import Base, engine, Session
from DB.models.rss import RSS
from utils.utils import un_healthy

Base.metadata.create_all(engine)
session = Session()
logger = logging.getLogger()


def db_persist(func):
    def persist(*args, **kwds):
        func(*args, **kwds)
        try:
            session.commit()
        except Exception as e:
            logger.error(e)
            session.rollback()
            un_healthy()
            return None

    return persist


@db_persist
def add_rss(rss):
    session.add(rss)


@db_persist
def update_last_check(rss, last_updated):
    rss.last_updated = last_updated


@db_persist
def de_active_channel(rss):
    rss.is_active = False


@db_persist
def remove_rss(rss):
    session.delete(rss)


def get_all_rss():
    return session.query(RSS).filter(RSS.is_active.is_(True)).all()


def get_rss_by_admin_chat_id(admin_chat_id):
    return session.query(RSS).filter(RSS.admin_chat_id == str(admin_chat_id)).all()


def get_rss_by_id(rss_id):
    return session.query(RSS).filter(RSS.id == rss_id).one_or_none()


def get_last_updated_rss():
    return session.query(RSS).order_by(RSS.last_updated).first()
