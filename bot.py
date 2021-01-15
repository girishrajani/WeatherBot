import discord 
import os
import requests
import json

from discord import message

apiKey = "" #API KEY

client = discord.Client()

def computeWeather(city):
    apiUrl = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey
    response = requests.get(apiUrl)
    data = response.json()
    weather = data['weather'][0]['main']
    desc = data['weather'][0]['description']
    returnOutput= "```City: "+city+"\n"+"Weather: "+weather+"\n"+"Description: "+desc+"```"
    return returnOutput
def computeTemp(city):
    apiUrl = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey
    response = requests.get(apiUrl)
    data = response.json()
    temp = data['main']['temp']
    temp = str(int((temp-273.15)//1))
    returnOutput = "```City: "+city+"\n"+"Temperature: "+temp+"```"
    return returnOutput
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
        await message.channel.send(output)
        return
    if message.content.startswith('#help'):
        helpMessage = "```HI My Name is Weather BOT"+"\n"+"Type #hello to say Hi"+"\n"+"Type #weather cityname to know about the weather"+"\n"+"Type #temp cityname to get the temperature```"
        await message.channel.send(helpMessage)
        return
    if message.content.startswith('#temp'):
        userMessage = message.content
        city = str(userMessage[5:])
        output = computeTemp(city)
        await message.channel.send(output)


#TOKEN KEY OF THE BOT
client.run("")
