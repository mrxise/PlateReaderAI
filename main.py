# AI that uses phone camera
# when aimed at a licence plate it detects the color (black white yellow green)
# read the digits
# sepeartes the digits
# recongnizes the wilaya
# recongnizes the manfiucatring year
# type of vehicle ()
# import os
import re
from tabulate import tabulate
from bs4 import BeautifulSoup as bs
import requests

req = requests.get("https://en.wikipedia.org/wiki/Template:Algeria_Wilayas")
# print(req)
soup = bs(req.text, "html.parser")

theTable = soup.find_all("td")
names = []
nums = []

for i, item in enumerate(theTable):
    raw = item.get_text().strip()
    if re.fullmatch(r"^[a-zA-Z'âéèï ]+$", raw):
        names.append(raw)
    if re.fullmatch(r'[1234567890]{1,2}', raw):
        nums.append(int(raw))
wilayas = list(zip(nums, names))
wilayas.sort(key=lambda x: x[0])
s = tabulate(wilayas)

print(s)
