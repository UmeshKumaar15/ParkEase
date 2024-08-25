import os
from twilio.rest import Client
import urllib.parse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_sms(phone_number):
    # Retrieve Twilio credentials from environment variables
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')  # Your Account SID from environment variable
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')    # Your Auth Token from environment variable

    # Create Twilio client
    client = Client(account_sid, auth_token)

    # UPI payment link details
    payee_vpa = os.getenv('UPI_PAYEE_VPA', "ultimateumesh15@oksbi")  # Default value provided
    payee_name = os.getenv('UPI_PAYEE_NAME', "PVR Parking Payment")  # Default value provided
    transaction_id = os.getenv('UPI_TRANSACTION_ID', "txn123456")  # Default value provided
    transaction_reference_id = os.getenv('UPI_TRANSACTION_REFERENCE_ID', "txn123456")  # Default value provided
    amount = os.getenv('UPI_AMOUNT', "10")  # Default value provided
    currency = os.getenv('UPI_CURRENCY', "INR")  # Default value provided

    # Create UPI link
    upi_link = (f"upi://pay?pa={urllib.parse.quote(payee_vpa)}&"
                f"pn={urllib.parse.quote(payee_name)}&"
                f"mc=0000&"  # Merchant Code (if used)
                f"tid={urllib.parse.quote(transaction_id)}&"
                f"tr={urllib.parse.quote(transaction_reference_id)}&"
                f"tn={urllib.parse.quote('Parking Payment Request #1234')}&"
                f"am={urllib.parse.quote(amount)}&"
                f"cu={urllib.parse.quote(currency)}")

    # Send SMS
    message = client.messages.create(
        body=f"Parking Payment Request, Please pay Rs. {amount} using the following UPI link: {upi_link}",
        from_=os.getenv('TWILIO_PHONE_NUMBER'),  # Your Twilio phone number from environment variable
        to=phone_number
    )

    print(f"Message SID: {message.sid}")
