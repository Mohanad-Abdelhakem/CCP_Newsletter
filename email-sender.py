import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_newsletter(email_list, subject, html_file_path):
    sender_email = "modestantonny@gmail.com" # Replace with your email
    sender_password = "mttc iizz uzgl csws" # Replace with your password

    # Set up the SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587) # this is the default port number and it's recommended here
    # we can replace host with the host provider's smtp server. For insrance, google is 'smtp.gmail.com'
    server.starttls()
    server.login(sender_email, sender_password)

    # Read HTML content from file
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    
    # Create the email
    for recipient in email_list:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(html_content, 'html'))

        # Send the email
        server.send_message(msg)

    server.quit()

# Example Usage
email_list = ["momedhat2005@gmail.com", "anhelina@uni.minerva.edu", "a.soliman@uni.minerva.edu", "jason@uni.minerva.edu", "clara@uni.minerva.edu", "hakkei@uni.minerva.edu"] # Replace with your list of emails
subject = "Weekly Newsletter - " + datetime.datetime.now().strftime("%Y-%m-%d")
html_file_path = "email-body.html"

send_newsletter(email_list, subject, html_file_path)
