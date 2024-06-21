import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import PIL
from cogs.render import Renderer

class GlobalCog(commands.Cog, name = "global"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["r"])
    async def render(self, ctx, *, objs = None):
        """renders the tiles specified"""
        if objs == None:
            await ctx.message.channel.send("input cant have 0 tiles")
            return
        grid = objs.split()
        width = objs[:objs.find("\n")].count(" ") + 1 # this is the worst thing i ever wrote in my entire life
        height = objs.count("\n") + 1
        success = Renderer.render(self, list(grid), (width, height))
        if isinstance(success, str):
            await ctx.message.channel.send(f"error: {success}!")
        else:
            await ctx.message.channel.send("not yet!!", file = discord.File("render.gif"))

async def setup(bot):
    await bot.add_cog(GlobalCog(bot))