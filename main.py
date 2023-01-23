# AI that uses phone camera
# when aimed at a licence plate it detects the color (black white yellow green)
# read the digits ********************
# sepeartes the digits *********************
# recongnizes the wilaya ***************
# recongnizes the manfiucatring year *******
# type of vehicle () ***************
# import os
import re
from bs4 import BeautifulSoup as bs
import requests

req = requests.get("https://en.wikipedia.org/wiki/Template:Algeria_Wilayas")
req2 = requests.get(
    "https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Algeria")
# print(req)
soup = bs(req.text, "html.parser")
soup2 = bs(req2.text, "html.parser")

theTable = soup.find_all("td")
VehType = soup2.find("ol").get_text().replace('\n', '').split()
names = [item.get_text().strip() for i, item in enumerate(
    theTable) if re.fullmatch(r"^[a-zA-Z'âéèï ]+$", item.get_text().strip())]
nums = [int(item.get_text().strip()) for i, item in enumerate(
    theTable) if re.fullmatch(r'[1234567890]{1,2}', item.get_text().strip())]
types = [veh for veh in enumerate(VehType, 1)]
# wilayas = list(zip(nums, names))
# wilayas.sort(key=lambda x: x[0])
wilayas = sorted(zip(nums, names), key=lambda x: x[0])


def slicer():

    while True:
        try:
            matricule = input("Enter your matricule: ")

            if not isinstance(matricule, str) or not re.fullmatch(r'\d{10}', matricule):
                raise ValueError("Invalide license plate")
            ser = matricule[:5]
            ann = matricule[5:8]
            wil = matricule[8:]

            def decodeAnne(ann):
                cheAn = ann[1:]
                cheType = int(ann[:1])
                for i, ty in types:
                    if cheType == i:
                        vType = cheType
                    elif cheType == 0:
                        print("Not registered yet")
                    if int(cheAn) < 50:
                        anneF = "20"+cheAn
                    else:
                        anneF = "19"+cheAn
                return anneF, vType
            an_, typeOf = decodeAnne(ann)
            return int(ser), an_, typeOf, int(wil)-1

        except ValueError as e:
            print(e)
            continue


serial, anne, typeOf, wil = slicer()
print(serial, anne, types[typeOf][1], wilayas[wil][1])
