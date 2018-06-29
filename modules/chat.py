import random
from discord.ext import commands

class ChatBot():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Hi')
    async def greet(self, ctx):
        await ctx.send(":smiley: :wave: Hello, there!")

    @commands.command()
    async def talk(self, ctx, sentence:str):
        await ctx.send("你刚说了 {}".format(sentence))

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title=self.name, description="Nicest bot there is ever.", color=0xeee657)
        # give info about you here
        embed.add_field(name="Author", value="<YOUR-USERNAME>")
        # Shows the number of servers the bot is member of.
        embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
        # give users a link to invite thsi bot to their server
        embed.add_field(
            name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ChatBot(bot))
