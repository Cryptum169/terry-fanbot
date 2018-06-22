import discord
from discord.ext import commands

class TerryBot():

    def __init__(self, cmd_prefix='$',botToken = None):
        if botToken == None:
            print('Did not pass in bot Token')
            exit()
        else:
            self.botToken = botToken
        self.name = 'Terry\'s Fan bot'
        self.cmd_prefix = cmd_prefix
        self.bot = commands.Bot(command_prefix=cmd_prefix)

    def load_bot(self):
        bot = self.bot
        @bot.event
        async def on_ready():
            print('Logged in as')
            print(bot.user.name)
            print(bot.user.id)
            print('------')

        @bot.command()
        async def adddd(ctx, a: int, b: int):
            await ctx.send(a+b)

        @bot.command()
        async def multiply(ctx, a: int, b: int):
            await ctx.send(a*b)

        @bot.command()
        async def greet(ctx):
            await ctx.send(":smiley: :wave: Hello, there!")

        @bot.command()
        async def cat(ctx):
            await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

        @bot.command()
        async def info(ctx):
            embed = discord.Embed(
                title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

            # give info about you here
            embed.add_field(name="Author", value="<YOUR-USERNAME>")

            # Shows the number of servers the bot is member of.
            embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

            # give users a link to invite thsi bot to their server
            embed.add_field(
                name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

            await ctx.send(embed=embed)

        bot.remove_command('help')

        @bot.command()
        async def help(ctx):
            embed = discord.Embed(
                title=self.name, description="A Very Nice bot. List of commands are:", color=0xeee657)

            embed.add_field(name=(cmd_prefix + "add X Y"),
                            value="Gives the addition of **X** and **Y**", inline=False)
            embed.add_field(name=(cmd_prefix + "multiply X Y"),
                            value="Gives the multiplication of **X** and **Y**", inline=False)
            embed.add_field(name=(cmd_prefix + "greet"),
                            value="Gives a nice greet message", inline=False)
            embed.add_field(name=(cmd_prefix + "cat"),
                            value="Gives a cute cat gif to lighten up the mood.", inline=False)
            embed.add_field(name=(cmd_prefix + "info"),
                            value="Gives a little info about the bot", inline=False)
            embed.add_field(name=(cmd_prefix + "help"),
                            value="Gives this message", inline=False)

            await ctx.send(embed=embed)

        bot.run(self.botToken)
