import discord
import json
from discord.ext import commands
import onready
import quoifeur
import music

cogs = [music, onready, quoifeur]

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

for i in range(len(cogs)):
    cogs[i].setup(bot)

with open('json/config.json') as jsondata:
    config = json.load(jsondata)

bot.run(config['token'])