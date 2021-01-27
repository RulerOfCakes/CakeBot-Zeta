import discord
import asyncio
from discord.ext import commands
from config.config import *
#TODO change directory name for the tokens

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    msg = message.content
#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!')
