import time
import sys
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# get start time
t0 = round(time.time(), 3)

# get global variables
dagname = sys.argv[1]
jobname = sys.argv[2]
machine_ip = sys.argv[3]
output_path = "/home/ubuntu/data/job/" + dagname

# email account credentials
email_user = 'email_address'
email_password = 'password'

# email contents
email_title = 'Result of Job: ' + jobname
email_body = 'Hi! \nAttached are the clustering results!'
receiver_email = 'email_address'

file1 = output_path + "/" + "result_sil_" + dagname + ".jpg"
file2 = output_path + "/" + "result_wss_" + dagname + ".jpg"
file3 = output_path + "/" + "result_time_" + dagname + ".jpg"
attachment_files = [file1, file2, file3]

# create the email message
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = receiver_email
msg['Subject'] = email_title

# attach the message body
msg.attach(MIMEText(email_body, 'plain'))

# attach files
for attachment_file in attachment_files:
    with open(attachment_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_file.split("/")[-1]}')
        msg.attach(part)

# send email
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email_user, email_password)
    server.sendmail(email_user, receiver_email, msg.as_string())
    server.close()
    print('Email sent successfully!')
except Exception as e:
    print('Error: ' + e)

t1 = round(time.time(), 3)
duration = round(t1-t0, 3)

# save live log
# log = 'dagname,jobname,machine_ip,start_time,end_time,duration,other_info\n'
log_file_path = output_path + "/" + 'log_' + dagname + '.txt'
log = (dagname + ',' + jobname + ',' + machine_ip + ',' + str(t0) + ',' + str(t1) + ',' + str(duration) + ',\n')
with open(log_file_path, 'a') as file:
    file.write(log)
