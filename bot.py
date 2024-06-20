import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import glob

import auth
import config

intents = discord.Intents.default()
intents.message_content = True

bot = discord.ext.commands.Bot(command_prefix = "=", intents = intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "=r..."))
    print(f"logged in as {bot.user}!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

async def load_cogs():
    for cog in config.cogs:
        try:
            await bot.load_extension(cog)
            print(f"loaded {cog}")
        except Exception as e:
            exc = f"{type(e).__name__}: {e}"
            print(f"failed to load {cog}: {exc}")

asyncio.run(load_cogs())
bot.run(auth.token)