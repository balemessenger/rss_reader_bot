from DB.models.base import Base, engine
from rss.state_handler import main

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main()
