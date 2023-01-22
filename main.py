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


matricule = "1234510140"
# for each in matricule:


def slicer():
    while True:
        try:
            matricule = input("Enter your matricule")

            if not isinstance(matricule, str) or not re.fullmatch(r'\d{10}', matricule):
                raise ValueError("Invalide license plate")
            ser = matricule[:5]
            ann = matricule[5:8]
            wil = matricule[8:]
            return int(ser), int(ann), int(wil)

        except ValueError as e:
            print(e)
            continue
        else:
            break


# 111 = Private 2011
#  199 = Private 1999
serial, anne, wil = slicer()
print(
    f"Your vehicle's serial number is {serial} and it was made in year {anne} and you are from {wilayas[wil-1]} ")
