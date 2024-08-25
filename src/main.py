import cv2
import torch
import time
from datetime import datetime
from dotenv import load_dotenv
from payment_request import send_sms
from json_utils import get_phone_number
from get_number import licensePlate_to_number

# Load environment variables
load_dotenv()


# Set a cooldown period (in seconds) to control how often we process frames
cooldown = 5

# Load the YOLOv5 model for license plate detection
model_path = 'model/LPDL_best.pt'  # Path to the YOLOv5 model file
model = torch.hub.load('D:/Bangalore codes/yolov5', 'custom', path=model_path, source='local')

# Open a connection to the default camera (0 for the built-in webcam)
cap = cv2.VideoCapture(0)

print("Starting video capture. Press 'q' to quit.")

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Perform detection on the captured frame
    results = model(frame)

    # Get bounding box coordinates of detected license plates
    coors = results.xyxy

    # Extract license plate number from the detected coordinates
    valid_number = licensePlate_to_number(frame, coors)

    if valid_number != "0":
        if valid_number != "Detection Unclear":
            curr_time = datetime.now()
            print(f"Detected Vehicle Number: {valid_number}")

            # Get the phone number associated with the detected license plate
            phone_number = get_phone_number(valid_number.replace(" ", ""))
            if phone_number != 0:
                # Send a UPI payment request SMS to the corresponding phone number
                send_sms(phone_number)
                print(f"Sent payment request to: {phone_number}")

            print(f"Vehicle Number: {valid_number}, In-Time: {curr_time}")

    # Check if 'q' key is pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Wait for the cooldown period before processing the next frame
    time.sleep(cooldown)

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

print("Video capture ended.")
