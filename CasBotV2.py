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
            message2 =  f"The current weather is {weatherData[0]}°C and the current feeling is {weatherData[1]}°C"
            await message.channel.send(message2)

        if user_message.lower() == "!rec_outfit":
            weatherData = json.loads(requests.get(weatherURL).content)
            outfit = appropriateClothing(weatherData)
            new_line = "\n"

            top = outfit[0]["item"]
            bottom = outfit[1]["item"]
            
            
            embed_message = discord.Embed(title="Recommended Outfit:", description=f"Recommended Top: {top}{new_line}Recommended Bottom: {bottom}",color=discord.Color.blue())
            embed_message.set_thumbnail(url="https://i.imgur.com/8oNmixC.jpg")
            embed_message.set_footer(text="These are the recommended outfits for the day. Have an amazing day!")

            await message.channel.send(embed=embed_message)

           
            

        #elif user_message.lower() == "!outfit":
            #pickOutfit()

client.run(TOKEN)