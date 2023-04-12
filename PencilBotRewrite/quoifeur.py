from discord.ext import commands
import json
from random import randint

with open('json/config.json') as jsondata:
        config = json.load(jsondata)

class quoifeur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        stripped_message = message.content.lower().strip(" .:?!*\)")
        #BannedWords
        if not message.author.id == self.bot.user.id:
            for bannedWord in config['bannedWords']:
                if bannedWord in message.content.lower():
                    await message.delete()

        #QuoiFeur
        for quoi in config['quoi']:
            if stripped_message.endswith(quoi):
                RandomVideoFeur = randint(1,10)
                await message.reply("feur")
                if RandomVideoFeur == 1:
                    await message.reply("http://askehraz.fr/upload/TheoFeur.mp4")
                elif RandomVideoFeur == 2:
                    await message.reply("http://askehraz.fr/upload/MinecraftFeur.mp4")
                else:
                    await message.reply("feur")
                    
        #WeebWord
        if not message.author.id == self.bot.user.id:
            for weebWords in config['weebWords']:
                if weebWords in message.content.lower():
                    await message.reply('ratio')

        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(quoifeur(bot))