import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from PIL import Image
import numpy
from io import BytesIO

class renderer:
    def __init__(self, bot):
        self.bot = bot

    def render(self, grid, grid_size, palette = "not yet handled!", delay = 200, frame_count = 3, upscale = 2):
        # takes a list of tiles (["baba", "wall", "wall", "keke"] for example) and renders it as a gif
        width, height = grid_size
        imgs = []
        for frame in range(frame_count):
            img_width = width * 24
            img_height = height * 24
            img = Image.new("RGBA", (img_width, img_height))
            imgs.append(img)
            gridind = 0
            for x in range(width):
                for y in range(height):
                    spr = Image.open(f"spr/baba/{grid[gridind]}_0_{frame + 1}.png").convert("RGBA")
                    if img is None:
                        return 0 # will return 0 if any errors happen
                    alpha = spr.getchannel("A")
                    imgs[frame].paste(spr, (x * 24, y * 24), mask = alpha)
                    gridind += 1
        ic = 0
        for i in imgs:
            imgs[ic] = i.resize((img_width * upscale, img_height * upscale), 0)
            ic += 1
        imgs[0].save("render.gif", save_all = True, append_images = imgs[1:], optimize = False, duration = 200, loop = 0, disposal = 2)

async def setup(bot):
    bot.renderer = renderer(bot)