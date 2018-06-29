import bot
import data.botSecret as bS

if __name__ == '__main__':
    terryBot = bot.TerryBot('&',bS.bot_token())
    terryBot.load_bot()