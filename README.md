# ParkEase

[![License](https://img.shields.io/badge/license-GNU%20GPL%20v3-blue)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Twilio](https://img.shields.io/badge/Twilio-API-purple)
![YOLOv5](https://img.shields.io/badge/YOLOv5-Model-green)

## Overview

**ParkEase** is an AI-powered, smart parking management system that automates license plate detection, OCR-based number extraction, and payment request processing. Using a custom-trained YOLOv5 model for accurate license plate detection, the system integrates seamlessly with Tesseract OCR for extracting text and sends UPI payment requests via SMS using Twilio.

## Features

- **License Plate Detection**: Utilizes a custom YOLOv5 model for high-accuracy license plate detection.
- **OCR and Pytesseract Integration**: Leverages Tesseract and OCR for extracting license plate numbers.
- **Automated Payment Request**: Sends UPI payment requests via SMS using Twilio, based on a JSON mapping of license plates to phone numbers.
- **Logging**: Logs detected license plates and timestamps to an Excel file for record-keeping.

## Accuracy

- **Model Performance**: The YOLOv5 detection model achieves:
  - **99.5% accuracy at mAP50**
  - **67.3% accuracy at mAP50:95**
- The model detects license plates and forwards the detected frames for number extraction.

![Detection Image](assets/model_result_img.jpg)

- The UPI request:
![UPI Image](assets/upi_image.jpeg)

## Installation

### Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Twilio Account](https://www.twilio.com/)
- Virtual Environment (`venv`)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/UmeshKumaar15/ParkEase.git
    cd ParkEase
    ```

2. **Set Up a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory:
    ```plaintext
    TWILIO_ACCOUNT_SID=your_account_sid
    TWILIO_AUTH_TOKEN=your_auth_token
    UPI_PAYEE_VPA=your_upi_vpa
    UPI_PAYEE_NAME=your_upi_name
    UPI_TRANSACTION_ID=your_transaction_id
    UPI_TRANSACTION_REFERENCE_ID=your_transaction_reference_id
    UPI_AMOUNT=10
    UPI_CURRENCY=INR
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    ```

5. **Run the System**:
    - To start the license plate detection and payment request system, run:
    ```bash
    python src/main.py
    ```

## Directory Structure

```plaintext
ParkEase/
│
├── model/
│   └── yolov5/                  
│       └── LPDL_best.pt                  # YOLOv5 model file
│
├── src/                         
│   ├── camera_yolov5.py                 # Script for capturing video and detecting license plates
│   ├── ocr_utils.py                     # Utilities for OCR processing
│   ├── json_utils.py                    # Functions for handling JSON operations
│   ├── excel_logger.py                  # Logs detected license plates to an Excel file
│   └── payment_request.py               # Handles sending payment requests via SMS
│
├── data/                        
│   ├── license_plate_logs.xlsx          # Excel file for logging detected license plates
│   └── license_plates_to_numbers.json   # JSON file mapping license plates to phone numbers
│
├── .env                                 # Environment variables (not included in the repository)
├── .gitignore                           # Ignore rules for Git
├── requirements.txt                     # Python dependencies
├── LICENSE                              # License file
└── README.md                            # Project README (this file)
```

## Contributing
Contributions are welcome! If you find a bug, have a feature request, or want to contribute in any way, feel free to open an issue or submit a pull request. We are open to accepting contributions from the community to make ParkEase even better!
