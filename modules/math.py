import discord
import math
from discord.ext import commands

class Math():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(ctx, a: int, b: int):
        await ctx.send(a+b)

    @commands.command()
    async def multiply(ctx, a: int, b: int):
        await ctx.send(a*b)

    @commands.command()
    async def power(ctx, a:int, b:int):
        await ctx.send(math.pow(a.b))

def setup(bot):
    bot.add_cog(Math(bot))