import discord 
import os
import requests
import json

from discord import message

client = discord.Client()

def computeWeather(city):
    
    return 
def computeTemp(city):

    return
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('#hello'):
        await message.channel.send("HELLO!")
        return
    if message.content.startswith('#weather'):
        userMessage = message.content
        city = str(userMessage[9:])
        output = computeWeather(city)
        await message.channel.send()
        return
    if message.content.startswith('#help'):
        helpMessage = "```HI My Name is Weather BOT"+"\n"+"Type #weather cityname to know about the weather"+"\n"+"Type #temp cityname to get the temperature```"
        await message.channel.send(helpMessage)
        return
    if message.content.startswith('#temp'):
        userMessage = message.content
        city = str(userMessage[5:])
        output = computeTemp(city)
        await message.channel.send()


#TOKEN KEY OF THE BOT
client.run("")
