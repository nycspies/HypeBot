from .handlers import HypeBot

def setup(bot):
  await bot.add_cog(HypeBot())
