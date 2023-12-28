import pandas as pd

def excel_writer(vehicle_number, in_time):
    excel_file_name = "C:\\Users\\umesh\\Documents\\AVLPRS_YOLOv5\\License_Plate_Logs.xlsx"

    try:
        # Read existing data from the Excel file
        existing_data = pd.read_excel(excel_file_name)

        # Get the maximum S.No and increment it
        max_s_no = existing_data['S.No'].max()
        new_s_no = max_s_no + 1 if not pd.isna(max_s_no) else 1

    except FileNotFoundError:
        # If the file doesn't exist, start with S.No = 1
        new_s_no = 1
        existing_data = pd.DataFrame()

    # Create a DataFrame with new data
    new_data = pd.DataFrame({'S.No': [new_s_no], 'Vehicle Number': [vehicle_number], 'In-Time': [in_time]})

    # Concatenate existing data with new data
    df = pd.concat([existing_data, new_data], ignore_index=True)

    # Write DataFrame to Excel file
    df.to_excel(excel_file_name, index=False)