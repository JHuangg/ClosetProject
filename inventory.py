import os
import sys
import json

with open('closet.json') as inv:
   closet_data = json.load(inv)

#print(closet_data)

def addItem():
    addItem = input('Enter the item you wish to add: ')
    addType = input('Enter the type of clothing: ')
    addColor = input('Color: ')
    addSize = input('Size: ')

    newItem = {'item': addItem, 'type': addType, 'color': addColor, 'size': addSize}
    closet_data.append(newItem)

    print(closet_data)

addItem()