from .handlers import HypeBot

async def setup(bot):
    await bot.add_cog(HypeBot(bot))
