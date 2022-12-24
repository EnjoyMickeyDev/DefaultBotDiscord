import os

import disnake
from disnake.ext import commands

class DefaultBotDiscord(commands.AutoShardedInteractionBot):
    def __init__(self):
        intents = disnake.Intents.default()

        super().__init__(
            intents=intents,
            activity=disnake.Activity(
                type=disnake.ActivityType.competing,
                name="https://metzker.tech",
                url="https://github.com/EnjoyMickeyDev"
            ),
        )
        self.developer = "Sabrina Spellman#0001"

    def load_extensions(self):
            for filename in os.listdir("./extensions"):
                if filename.endswith(".py"):
                    try:
                        self.load_extension(f"extensions.{filename[:-3]}")
                        print(f'[Extensions]: {filename} loaded...')
                    except Exception as e:
                        print(e)