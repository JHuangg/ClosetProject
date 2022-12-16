import discord
from discord.ext import commands
import json
from weather import *
from productRecommendation import *
import requests
import random
import os

weather = 35

# TOKEN = 
CMD_PREFIX = "!"

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
# API_KEY = 
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

        if user_message.lower() == "!review_product":
            await message.channel.send("Please enter a product link")
            try:
                response = await client.wait_for("message", timeout=60.0)
            except:
                await message.channel.send("Sorry please respond faster with a URL! 60 second timeout")
            
            # take product and scrape lulu site
            os.system(f'scrapy crawl lulu -o reviews.txt -a url={response.content}')

            #results are now placed in reviews.txt
            product_sentiment = provide_sentiment()
            await message.channel.send(f"Your product has the following sentiment: {product_sentiment}")

        if user_message.lower() == "!suggest":
            await message.channel.send("Please send a photo of desired outfit")

client.run(TOKEN)