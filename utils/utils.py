from main_config import BotConfig


def un_healthy():
    try:
        with open(BotConfig.heathens_path, "w") as file:
            file.truncate(0)
            file.write("0")
            file.close()
    except:
        un_healthy()


def healthy():
    try:
        with open(BotConfig.heathens_path, "w") as file:
            file.truncate(0)
            file.write("1")
            file.close()
    except:
        un_healthy()
