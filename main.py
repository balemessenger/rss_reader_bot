from DB.models.base import Base, engine
from rss.state_handler import main
from utils.utils import un_healthy, healthy

if __name__ == '__main__':
    try:
        healthy()
        Base.metadata.create_all(engine)
        main()
    except:
        un_healthy()
