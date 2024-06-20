import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

class cog_test(commands.Cog, name = "test"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def boom(self, ctx):
        await ctx.message.channel.send("gooby")
        await self.bot.close()

    @commands.command(aliases = ["rr"])
    @commands.is_owner()
    async def reload(self, ctx):
        cogs = [a for a in self.bot.extensions.keys()]
        for cog in cogs:
            await self.bot.reload_extension(cog)
        await ctx.send("reloaded all extensions:tada:")

async def setup(bot):
    await bot.add_cog(cog_test(bot))