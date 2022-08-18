import discord
import json

# Function to convert kelvins to celsius
def convertTemp(kelvin):
    return(kelvin - 273.15)

def parseData(data):
    dataMain = data['main']
    kelvinTemp = dataMain['temp']
    kelvinFeelingTemp = dataMain['feels_like']
    currentTemp = int(convertTemp(kelvinTemp))
    currentFeeling = int(convertTemp(kelvinFeelingTemp))
    return (f"The current weather is {currentTemp}°C and the current feeling is {currentFeeling}°C")

def appropriateClothing(weather, weatherDescription):
    clothingRecommendations = []
    with open('closet.json') as inv:
        closet_data = json.load(inv)
    
    if weather <= 0 or weatherDescription == 'snowing':
        for item in closet_data:
            if item['type'] == "Jacket" or item['type'] == "Boots":
                clothingRecommendations.append(item)

    elif 0 < weather <= 21:
        for item in closet_data:
            if item['type'] == "Sweater":
                clothingRecommendations.append(item)
    else:
        for item in closet_data:
            if item['type'] == "Shirt":
                clothingRecommendations.append(item)

    return clothingRecommendations

print(appropriateClothing(-42, "nothing"))
