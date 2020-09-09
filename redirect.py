import time
import sounddevice as sd
import numpy as np
from loguru import logger
import smtplib
from email.mime.multipart import MIMEMultipart


def send_mail():
    # The mail addresses and password
    time.sleep(2)
    sender_address = 'lauper.bms@mail.ch'
    sender_pass = 'TbzTbz123'
    receiver_address = 'moritz.lauper@hispeed.ch'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'back to work!'
    try:
        session = smtplib.SMTP('smtp.mail.ch', 587)
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('back to work!')
    except:
        logger.info('Mail could not be sent.')


def volume(indata, outda, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if int(volume_norm) >= 2:
        send_mail()


while True:
    with sd.Stream(callback=volume):
        sd.sleep(100)
