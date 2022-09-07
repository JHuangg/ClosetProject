import discord
from discord.ext import commands
import json
from weather import *
import requests
import random

weather = 35

TOKEN = 'MTAwODg2NTMzMzMzNzE0NTM0NQ.GAW5jL.Ez9XYFCnOwQ2SZ9eQUsPcLkikrAYJXhHoJfehw'
CMD_PREFIX = "!"

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = 'd98de545923f862fce0481797ebdf2dc'
CITY = 'Toronto'
weatherURL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author != client.user and message.content.startswith(CMD_PREFIX):
        if user_message.lower() == "!weather":
            weatherData = json.loads(requests.get(weatherURL).content)
            weatherData = parseTemp(weatherData)
            message =  f"The current weather is {weatherData[0]}°C and the current feeling is {weatherData[1]}°C"
            await message.channel.send(message)

        if user_message.lower() == "!rec_outfit":
            weatherData = json.loads(requests.get(weatherURL).content)
            outfit = appropriateClothing(weatherData)

        #elif user_message.lower() == "!outfit":
            #pickOutfit()

client.run(TOKEN)