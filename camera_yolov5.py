import cv2
import torch
import time

from datetime import datetime
from getNumber import licensePlate_to_number
from write_to_excel import excel_writer

cooldown = 5

# Load the model
model = torch.hub.load('.', 'custom', path='runs/train/exp2/weights/last.pt', source='local')

# Open a connection to the webcam (0 corresponds to the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Perform inference on the frame
    results = model(frame)

    # Access bounding box coordinates
    coors = results.xyxy

    # Call getOCR if something is detected
    valid_number = licensePlate_to_number(frame, coors)
    if valid_number != "0":
        if valid_number != "Detection Unclear":
            curr_time = datetime.now()
            excel_writer(valid_number, str(curr_time))
            print("Vehicle Number: ", valid_number, ", In-Time: ", curr_time )
   
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(cooldown)

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()