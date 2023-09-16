import discord
import asyncio
from discord.ext import commands
from configparser import ConfigParser
from tree import build_tree
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

#Example quiz command I put together because I couldnt sleep - DJ
#arg unused for now, could use it to show past results/answers?
@client.command()
async def quiz(ctx, arg):
    root_node = build_tree()
    active_node = root_node
    await ctx.reply(f'Hello {ctx.author.name}. Beginning Quiz!')
    await asyncio.sleep(1)

    #active node's data is the current question being asked
    msg = ""
    #Forces user to type 1 or 2, there are more elegant ways of doing this, like reaction monitoring.
    while msg != "1" and msg != "2":
        await ctx.reply(f'{active_node.data}')
        msg = await client.wait_for('message', check=check(ctx.author), timeout=30)
        #blahblahblah

#Checks if author of message is the author of the original message too
def check(author):
    def inner_check(message):
        if message.author != author:
            return False
        
        return True
    return inner_check
#Starts the bot.
client.run(TOKEN)