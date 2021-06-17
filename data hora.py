# Mostrador de Data e Hora renováveis a cada 60 segundos

from _datetime import datetime
import time

datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
while True:
    if datetime.now().strftime('%d-%m-%Y %H:%M:%S') == datetime.now().strftime('%d-%m-%Y %H:%M:00'):
        print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        time.sleep(60)
