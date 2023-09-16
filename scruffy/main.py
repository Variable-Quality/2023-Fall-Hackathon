import discord
from discord.ext import commands
from configparser import ConfigParser

cfg = ConfigParser()

#Somehow this works on windows? Not sure if configparser is just that good or something else is going on
#Def need to test this before deploying
cfg.read('secret.ini')
TOKEN = cfg['DEFAULT']['TOKEN']

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

#This 
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def test(ctx):
    print(ctx.__dict__)


client.run(TOKEN)