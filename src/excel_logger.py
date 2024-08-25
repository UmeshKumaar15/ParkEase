import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the path to the Excel file from environment variables
EXCEL_FILE_PATH = os.getenv('EXCEL_FILE_PATH')

def excel_writer(vehicle_number, in_time):
    try:
        # Read existing data from the Excel file
        existing_data = pd.read_excel(EXCEL_FILE_PATH)

        # Get the maximum serial number and increment it
        max_s_no = existing_data['S.No'].max()
        new_s_no = max_s_no + 1 if not pd.isna(max_s_no) else 1

    except FileNotFoundError:
        # If the file doesn't exist, start with S.No = 1
        new_s_no = 1
        existing_data = pd.DataFrame()

    # Create a DataFrame with new data
    new_data = pd.DataFrame({
        'S.No': [new_s_no],
        'Vehicle Number': [vehicle_number],
        'In-Time': [in_time]
    })

    # Concatenate existing data with new data
    df = pd.concat([existing_data, new_data], ignore_index=True)

    # Write DataFrame to Excel file
    df.to_excel(EXCEL_FILE_PATH, index=False)
    print(f"Logged vehicle number {vehicle_number} at {in_time}")

# Example usage (comment out in production)
# excel_writer("KA01AB1234", "2024-08-25 12:34:56")
