from os import getenv

class Config(object):
      API_HASH = getenv("93ba4db0ad662e558356871afe8ca6de")
      API_ID = int(getenv("7851526", 0))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "5741250423:AAG_NPgUPrAncCRddyBoEmRr0K_5a7Uh_4I")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
