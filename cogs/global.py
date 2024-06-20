import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import PIL
from cogs.render import renderer

class cog_global(commands.Cog, name = "global"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["r"])
    async def render(self, ctx):
        renderer.render(self, ["baba", "arrow", "cash", "rock"], (2, 2))
        await ctx.message.channel.send("not yet!!", file = discord.File("render.gif"))

async def setup(bot):
    await bot.add_cog(cog_global(bot))