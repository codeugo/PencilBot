from discord.ext import commands

class onready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Pencil-Bot is ready!')

def setup(bot):
    bot.add_cog(onready(bot))