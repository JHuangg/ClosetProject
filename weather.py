import discord

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