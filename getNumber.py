import cv2
import string
import easyocr
import pytesseract

# Specify the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/umesh/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

#States Dict for Verification of detected number
state_dict = {
    'AS': 'Assam',
    'AR': 'Arunachal Pradesh',
    'BR': 'Bihar',
    'AN': 'Andaman and Nicobar Islands',
    'CH': 'Chandigarh',
    'CG': 'Chhattisgarh',
    'GJ': 'Gujarat',
    'DN': 'Dadra and Nagar Haveli',
    'DD': 'Daman and Diu',
    'GA': 'Goa',
    'HR': 'Haryana',
    'HP': 'Himachal Pradesh',
    'JH': 'Jharkhand',
    'JK': 'Jammu and Kashmir',
    'KA': 'Karnataka',
    'KL': 'Kerala',
    'MH': 'Maharashtra',
    'MP': 'Madhya Pradesh',
    'MN': 'Manipur',
    'ML': 'Meghalaya',
    'MZ': 'Mizoram',
    'LD': 'Lakshadweep',
    'DL': 'National Capital Territory of Delhi',
    'NL': 'Nagaland',
    'PY': 'Puducherry',
    'OD': 'Odisha',
    'PB': 'Punjab',
    'SK': 'Sikkim',
    'RJ': 'Rajasthan',
    'TN': 'Tamil Nadu',
    'TR': 'Tripura',
    'UK': 'Uttarkhand',
    'UP': 'Uttar Pradesh'
}

# Function to perform OCR on a region of interest
def licensePlate_to_number(im, coors):
        
    # Extracting the first set of coordinates if there are multiple detections
    if coors:
        coors_list = coors[0].cpu().numpy()

        # Check if the list is not empty
        if len(coors_list) > 0:
            # Extracting x, y, w, h from the first row of the tensor
            x, y, w, h, _, _ = coors_list[0]
        else:
            return "0"
    else:
        return "0"

    x, y, w, h = int(x), int(y), int(w), int(h)
    plate_image = im[y:h, x:w]

    # plate_image = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    cv2.imshow("plate", plate_image)
    OCR_output = getOCR(plate_image)
    Tesseract_output = getTesseract(plate_image)

    if OCR_output is not None or Tesseract_output is not None:
        return check_valid_number(OCR_output, Tesseract_output)
    else:
        return "Detection Unclear"


def getOCR(img):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(img)
    ocr = ""
    for res in result:
        if len(res) > 1 and len(res[1]) > 6:
            ocr = res[1]
    return str(ocr)

def getTesseract(img):
    result = pytesseract.image_to_string(img,lang='eng')
    return str(result)

def remove_trailing_leading_characters(value):
    alp_value = ''.join(char for char in value if char.isalnum())
    
    if alp_value:
        return alp_value
    else:
        return None

def check_valid_number(n1 = "", n2 = ""):
    output_arr = [n1, n2]
    score_arr = [0, 0]

    for i in range(len(output_arr)):
        test_num = output_arr[i]
        test_num = remove_trailing_leading_characters(test_num)
        
        if test_num is not None:
            if len(test_num) >= 10:
                score_arr[i] += 10
            else:
                continue
        else:
            continue
        
        if test_num[0:2].upper() in state_dict:
            score_arr[i] += 10
        
        if ord(test_num[2]) <  58:
            score_arr[i] += 1
        
        if ord(test_num[3]) <  58:
            score_arr[i] += 1

        if ord(test_num[4]) >  58:
            score_arr[i] += 1

        if ord(test_num[5]) >  58:
            score_arr[i] += 1

        if ord(test_num[6]) <  58:
            score_arr[i] += 1
        
        if ord(test_num[7]) <  58:
            score_arr[i] += 1

        if ord(test_num[8]) < 58:
            score_arr[i] += 1

        if ord(test_num[9]) <  58:
            score_arr[i] += 1

    valid_number = output_arr[score_arr.index(max(score_arr))]

    if len(valid_number) > 10:
        valid_number = valid_number[0:10]

    return valid_number.upper()