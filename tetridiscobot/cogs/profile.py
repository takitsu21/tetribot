from discord.ext import commands

class Profile(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx):
        await ctx.send("Hello World!")

def setup(bot):
    bot.add_cog(Profile(bot))