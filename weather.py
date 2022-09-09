import discord
import json

# Function to convert kelvins to celsius
def convertTemp(kelvin):
    return(kelvin - 273.15)

def parseTemp(data):
    dataMain = data['main']
    kelvinTemp = dataMain['temp']
    kelvinFeelingTemp = dataMain['feels_like']
    currentTemp = int(convertTemp(kelvinTemp))
    currentFeeling = int(convertTemp(kelvinFeelingTemp))
    return [currentTemp,currentFeeling]

def appropriateClothing(data):
    clothingRecommendations = []
    with open('closet.json') as inv:
        closet_data = json.load(inv)

    dataMain = data['main']
    kelvinTemp = dataMain['temp']
    currentTemp = int(convertTemp(kelvinTemp))

    dataWeather = data['weather']
    dataDescription = dataWeather[0]['description']
    
    if currentTemp <= 0 or dataDescription == 'snowing':
        for item in closet_data:
            if item['type'] == "Jacket" or item['type'] == "Boots":
                clothingRecommendations.append(item)

    elif 0 < currentTemp <= 21:
        for item in closet_data:
            if item['type'] == "Sweater":
                clothingRecommendations.append(item)
            elif item['type'] == "Pants":
                clothingRecommendations.append(item)
    else:
        for item in closet_data:
            if item['type'] == "Shirt":
                clothingRecommendations.append(item)

    return clothingRecommendations

