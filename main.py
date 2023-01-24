import re
from bs4 import BeautifulSoup
import requests
import cam

req = requests.get("https://en.wikipedia.org/wiki/Template:Algeria_Wilayas")
req2 = requests.get(
    "https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Algeria")
soup = BeautifulSoup(req.text, "html.parser")
soup2 = BeautifulSoup(req2.text, "html.parser")

# Extract the wilaya names and numbers from the table
tds = soup.find_all("td")
names = [td.get_text().strip() for td in tds if re.fullmatch(
    r"^[a-zA-Z'âéèï ]+$", td.get_text().strip())]
nums = [int(td.get_text().strip()) for td in tds if re.fullmatch(
    r'[1234567890]{1,2}', td.get_text().strip())]

# Extract the vehicle types
VehType = soup2.find("ol").get_text().splitlines()
types = [(i, " ".join(veh.split())) for i, veh in enumerate(VehType, 1)]


# Sort the wilayas by number
wilayas = sorted(zip(nums, names), key=lambda x: x[0])


def slicer(matricule):
    while True:
        try:
            # matricule = input("Enter your matricule: ")
            if not isinstance(matricule, str) or not re.fullmatch(r'\d{10}', matricule):
                raise ValueError("Invalid license plate")
            ser = matricule[:5]
            ann = matricule[5:8]
            wil = matricule[8:]

            # Decode the year and vehicle type from the matricule
            def decodeAnne(ann):
                cheAn = ann[1:]
                cheType = int(ann[:1])
                for i, ty in types:
                    if cheType == i:
                        vType = ty
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


res = cam.res
for i in range(len(res)):
    serial, anne, typeOf, wil = slicer(res[i])
    print(
        f"Car number {i+1} has a serial of: {serial} registered in: {wilayas[wil][1]}\nFabrucated in: {anne}\nIt's a: {typeOf}\n")
