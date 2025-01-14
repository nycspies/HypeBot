from redbot.core import commands

class HypeBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hype(self, ctx):
        await ctx.send("Let's get hyped!")

async def setup(bot):
    cog = HypeBot(bot)
    await bot.add_cog(cog)  # Make sure this is awaited!
