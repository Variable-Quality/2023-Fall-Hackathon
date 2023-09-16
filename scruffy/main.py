import discord
from discord.ext import commands
from configparser import ConfigParser

cfg = ConfigParser()

#Somehow this works on windows? Not sure if configparser is just that good or something else is going on
#Def need to test this before deploying
cfg.read('secret.ini')
TOKEN = cfg['DEFAULT']['TOKEN']

#This makes the bot able to read messages
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def test(ctx):
    #User types !test, bot prints the context dict out to the console
    print(ctx.__dict__)

#Starts the bot.
client.run(TOKEN)