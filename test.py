import os
from datetime import datetime

try:
    filename = str(datetime.now().date())
    file = open(filename+".txt", "r")
    file.close()
except FileNotFoundError:
    print(filename)