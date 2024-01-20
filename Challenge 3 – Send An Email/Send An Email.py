import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

load_dotenv()

def send_email():
    # Email configuration
    app_password = "ctti qivq ueue lfjs"
    receiver_email = "hr@ignitershub.com"
    subject = "Challenge 3 Completed"
    port = 465

    # Your information
    name = "Aman Kumar"
    semester = "8"
    branch = "CS"
    roll_number = "200"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = "kumaramanme@gmail.com"
    message["To"] = receiver_email
    message["Subject"] = subject

    # Body of the email
    body = f"""
    Name: {name}
    Semester: {semester}
    Branch: {branch}
    Roll Number: {roll_number}
    """
    message.attach(MIMEText(body, "plain"))

    # Attach an image 
    image_path = 'D:\\doctorBg.jpg'
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name="image.png")
        message.attach(image)

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
            server.login("kumaramanme@gmail.com", app_password)
            server.sendmail("kumaramanme@gmail.com", receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

if __name__ == "__main__":
    send_email()
