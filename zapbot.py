import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+552899979-5356', '+5528999950128']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'koleeeeeeeeeee, testando meu bot', datetime.now().hour, datetime.now().minute + 2)
    del contatos[0]
    time.sleep(15)
    keyboard.press_and_release('enter')
    time.sleep(20)
    keyboard.press_and_release('ctrl + w')