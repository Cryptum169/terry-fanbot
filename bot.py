import discord
from discord.ext import commands
import os

class TerryBot(commands.AutoShardedBot):

    def __init__(self, cmd_prefix='$', botToken=None):
        super().__init__(command_prefix=cmd_prefix,  # commands.when_mentioned_or('n!')
                         description="Terry-Fanbot",
                         pm_help=None,
                         shard_id=0,
                         status=discord.Status.dnd,
                         activity=discord.Game(name="Restarting..."),
                         fetch_offline_members=False,
                         max_messages=2500,
                         help_attrs={'hidden': True})

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

        @bot.command(name='Hi')
        async def greet(ctx):
            await ctx.send(":smiley: :wave: Hello, there!")

        bot.remove_command('help')

        @bot.command()
        async def help(ctx):
            embed = discord.Embed(
                title=self.name, description="A Very Nice bot. List of commands are:", color=0xeee657)
            embed.add_field(name=(self.cmd_prefix + "add X Y"),
                            value="Gives the addition of **X** and **Y**", inline=False)
            embed.add_field(name=(self.cmd_prefix + "multiply X Y"),
                            value="Gives the multiplication of **X** and **Y**", inline=False)
            embed.add_field(name=(self.cmd_prefix + "greet"),
                            value="Gives a nice greet message", inline=False)
            embed.add_field(name=(self.cmd_prefix + "cat"),
                            value="Gives a cute cat gif to lighten up the mood.", inline=False)
            embed.add_field(name=(self.cmd_prefix + "info"),
                            value="Gives a little info about the bot", inline=False)
            embed.add_field(name=(self.cmd_prefix + "help"),
                            value="Gives this message", inline=False)
            await ctx.send(embed=embed)

        for file in os.listdir("modules"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.bot.load_extension(f"modules.{name}")
                    print('Sucessfully Loaded {}'.format(name))
                except:
                    exc = '{}: {}'.format(type(e).__name__, e)
                    print('Failed to load extension {}\n{}'.format(extension, exc))

        bot.run(self.botToken)
