# License Plate Detection and Logging using YOLOv5

[![License](https://img.shields.io/badge/license-GNU%20GPL%20v3-blue)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)


## Overview


This project utilizes a customized YOLOv5 model for accurate license plate detection, integrated seamlessly with OCR (Optical Character Recognition) using pytesseract. The system is designed to efficiently extract license plate information and features an automated logging to an excel file.

## Features

- License plate detection using a Custom YOLOv5 model.
- OCR and pytesseract integration for extracting text from detected license plates.
- Implemented a validation process to choose the best license plate number out of the results obtained from OCR and pytesseract.
- Automated logging system for storing license plate information to an excel file.
- Customizable and extendable for specific use cases.

## Accuracy
- The Detection model has an accuracy of **99.5% at mAP50** and **67.3% at mAP50:95**.
- The Detection model only detects the License plate and it sends the detected frame of license plate for number extraction.

  <img src="model_result_img.jpg" alt="Sample Image" width="500"/>


## Installation
Follow the below steps for setting up this system:
- Clone this repo (License-Plate-detection-and-logging-using-YOLOv5) using
-     git clone https://github.com/UmeshKumaar15/License-Plate-detection-and-logging-using-YOLOv5.git
  
- Open command prompt and change directory to that new folder using
-     cd License-Plate-detection-and-logging-using-YOLOv5
  
-  Now Install the dependencies listed in the requirements.txt file using the following command:
-      pip install -r requirements.txt
  
-  Now clone yolov5 repo using command
-     git clone https://github.com/ultralytics/yolov5.git

- After cloning the repo, enter into yolov5 folder using
-     cd yolov5
  
-  The yolov5 folder contains important python file called detect.py which is responsible to detect the objects.
  
- Install all the necessary requirements using
-     pip install -r requirements.txt
  
- Now the model "LPDL_best.pt" is ready to detect the license plates using the command
-     python detect.py --weights LPDL_best.pt --img-size 640 --source 0
  
- Source 0 starts Live Webcam for Realtime-Detection
- You can also test the model using local image/video file by replacing the 0 at source with file path.
- Once the test detection is successfull, we can implement this system by running camera_yolov5, which detects the plates, extracts their number and stores their details with time to an local excel file.



## Contributing

Contributions are welcome! If you find a bug, have a feature request, or want to contribute in any way, feel free to open an issue or submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-or-bugfix-name`.
3. Make your changes and commit them: `git commit -m 'Your commit message'`.
4. Push to your branch: `git push origin feature-or-bugfix-name`.
5. Open a pull request against the `main` branch.

### Bug Reports

If you encounter any issues, please open an issue with a detailed description of the problem. Include steps to reproduce, if possible.

### Feature Requests

If you have ideas for new features or improvements, open an issue to discuss them. Your input is valuable!

### Code Style

Please follow the existing code style in the project. If you're unsure, feel free to ask.

Thank you for contributing!
