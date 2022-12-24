import os

from dotenv import load_dotenv
from core.defaultbotdiscord import DefaultBotDiscord

load_dotenv()

bot = DefaultBotDiscord()
bot.load_extensions()
bot.run(os.getenv("TOKEN"))
