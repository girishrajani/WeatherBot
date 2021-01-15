import discord 
import os

from discord import message

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('#hello'):
        await message.channel.send("HELLO!")

# client.run(os.getenv("TOKEN"))