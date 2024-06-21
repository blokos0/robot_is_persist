import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

class TestCog(commands.Cog, name = "test"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def boom(self, ctx):
        """kills the bot"""
        await ctx.message.channel.send("gooby")
        await self.bot.close()

    @commands.command(aliases = ["rr"])
    @commands.is_owner()
    async def reload(self, ctx):
        "reloads all of the bots extensions"""
        cogs = [a for a in self.bot.extensions.keys()]
        for cog in cogs:
            await self.bot.reload_extension(cog)
        await ctx.send("reloaded all extensions:tada:")

async def setup(bot):
    await bot.add_cog(TestCog(bot))