import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\PCµ\AppData\Local\TCR\tesseract.exe'

# Specify the path to the image file
file_path = ".\image\imageup.png"


# Read the image from file
image = cv2.imread(file_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Run OCR on the image
numbers = pytesseract.image_to_string(thresh, config='--psm 11')

res = numbers.replace(" ", "").split()
# print(res)
