import calendar
import sys
from datetime import datetime
import os
import json

# Json file for calendar
with open("calendar_data.json", "r") as json_file:
    data = json.load(json_file)
