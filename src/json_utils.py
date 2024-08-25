import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the path to the JSON file
json_file_path = os.path.join("data", "license_plates_to_numbers.json")

# Load the JSON file with license plate mappings
with open(json_file_path, 'r') as file:
    license_plate_dict = json.load(file)

# Function to get phone number based on license plate
def get_phone_number(license_plate):
    return license_plate_dict.get(license_plate, 0)

# Function to add or update a license plate entry
def add_or_update_license_plate(license_plate, phone_number):
    license_plate_dict[license_plate] = phone_number
    # Save the updated dictionary to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(license_plate_dict, file, indent=4)
    print(f"Added/Updated: {license_plate} -> {phone_number}")
