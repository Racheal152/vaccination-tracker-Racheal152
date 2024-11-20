import smtplib
from email.mime.text import MIMEText

def send_email_reminder(email, subject, body):
    # Configure your email settings
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"     # Replace with your email password or app-specific password

    try:
        # Create MIMEText object for the email body
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email

        # Set up the SMTP server (Gmail in this case)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to your Gmail account
            server.sendmail(sender_email, email, msg.as_string())  # Send the email

        print(f"Reminder sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Example usage
send_email_reminder("recipient@example.com", "Vaccination Reminder", "Please get vaccinated soon!")
