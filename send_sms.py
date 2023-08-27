import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
SMTP_SERVER = os.environ.get('SMTP_SERVER')
PORT = os.environ.get('PORT')

def send_sms(phone_number, message):
    email = EMAIL
    password = PASSWORD
    smtp_server = SMTP_SERVER
    smtp_port = PORT
    
    # Create a dictionary to map carriers to their email-to-SMS gateway domains
    carrier_gateways = {
        'AT&T': 'txt.att.net',
        'Verizon': 'vtext.com',
        'T-Mobile': 'tmomail.net',
        'Sprint': 'messaging.sprintpcs.com',
        # Add more carriers and gateways as needed
    }
    
    # Extract the carrier from the phone number
    carrier = 'T-Mobile'  # Replace with actual carrier
    
    if carrier in carrier_gateways:
        gateway_domain = carrier_gateways[carrier]
        to_email = f'{phone_number}@{gateway_domain}'
    else:
        print(f"Carrier '{carrier}' not found in the list.")
        return
    
    # Compose the email message
    subject = 'Test Message'
    body = message
    email_text = f'Subject: {subject}\n\n{body}'
    
    # Send the email
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.set_debuglevel(1)  # Enable debugging
        server.login(email, password)
        server.sendmail(email, to_email, email_text)
        server.quit()
        print(f"Message sent successfully to {phone_number}")
    except Exception as e:
        print(f"Error sending message to {phone_number}: {e}")

def main():
    phone_numbers = []
    
    # Read phone numbers from the file
    with open('phone_numbers.txt', 'r') as file:
        for line in file:
            phone_numbers.append(line.strip())  # Remove newline characters
    
    message = "Hello, this is an SMS message sent via email!"
    
    # Send messages to each phone number
    for phone_number in phone_numbers:
        send_sms(phone_number, message)

if __name__ == "__main__":
    main()