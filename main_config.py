import os


class BotConfig:
    redis_host = os.getenv('REDIS_HOST', "localhost")
    redis_port = int(os.getenv('REDIS_PORT', 6379))
    redis_db = os.getenv('REDIS_DB', 0)
    connection_pool_size = int(os.environ.get('CONN_POOL', 50))
    heathens_path = os.path.dirname(os.path.abspath(__file__))+"/aliveness"
    poll_interval = float(os.environ.get('POLL_INTERVAL', 0.5))
    rss_count = int(os.environ.get('RSS_COUNT', 4))
    rss_interval = float(os.environ.get('RSS_INTERVAL', 5))
    token = os.environ.get('TOKEN', "token")
    base_file_url = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")


class DatabaseConfig:
    db_user = os.getenv('POSTGRES_USER', "ehsan")
    db_password = os.getenv('POSTGRES_PASSWORD', "ehsan1379")
    db_host = os.getenv('POSTGRES_HOST', "localhost")
    db_name = os.getenv('POSTGRES_DB', "rss_bot")
    db_port = os.getenv('POSTGRES_PORT', "5432")
    database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name) or None
