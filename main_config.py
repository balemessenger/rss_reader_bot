import os


class BotConfig:
    poll_interval = float(os.environ.get('POLL_INTERVAL', 0.5))
    rss_interval = int(os.environ.get('RSS_INTERVAL', 5))
    token = os.environ.get('TOKEN', "2063839091:6fcac9a53e5a7cbcd7e2c71abfcdba3d4c5ece88")
    base_file_url = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")


class DatabaseConfig:
    db_user = os.getenv('POSTGRES_USER', "ehsan")
    db_password = os.getenv('POSTGRES_PASSWORD', "ehsan1379")
    db_host = os.getenv('POSTGRES_HOST', "localhost")
    db_name = os.getenv('POSTGRES_DB', "rss_bot")
    db_port = os.getenv('POSTGRES_PORT', "5432")
    database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name) or None