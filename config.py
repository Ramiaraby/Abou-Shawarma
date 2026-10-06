from Bot.bot import Bot

prefix = '!'
bot_name = 'Abou Shawarma'

with open("bot token.txt", "r", encoding="utf-8") as f:
    bot_token = f.read().strip()

bot = Bot(prefix=prefix)