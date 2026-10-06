import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self, prefix):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        print('------')