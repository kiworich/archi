import datetime
from voice import *
from datetime import datetime
import time
import webbrowser
import os
import sys
from bs4 import BeautifulSoup
import requests
import subprocess
from subprocess import run, Popen, PIPE
import logging

city = ''
link = f"https://www.google.com/search?q=погода+в+{city}"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

hello = ['привет', 'hey', 'hello', 'здравствуй']
times = ['время', 'сколько времени', 'какое время', 'time']
vk = ['открой вк', 'открой vk', 'вк', 'vk']
youtube = ['youtube', 'открой youtube']
bye = ['пока','прошай','пока пока']
telegram = ['телеграм', 'telegram', 'открой телеграм', 'открой telegram']
steam = ['steam', 'стим', 'открой стим', 'открой steam']
discord = ['discord', 'открой discord', 'открой дискорд', 'дискорд']
weather = ['weather', 'погода', 'какая погода']
date = ['date', 'дата', 'какая дата']

def archi():
    command = take_command()
    print(command)
    if command in hello:
        talk('ку')
    elif command in times:
        t = time.localtime() 
        current_time = time.strftime("%H:%M:%S", t) 
        talk(current_time)
    elif command in date:
        current_date = datetime.now().date()
        talk(current_date)
    elif command in bye:
        talk('bye bye')
        sys.exit()
    elif command in weather:
        responce = requests.get(link, headers=headers)
        print(responce)

        f = '<Response [200]>'

        soup = BeautifulSoup(responce.text, "html.parser")


        # Парсим погоду
        temperature = soup.select("#wob_tm")[0].getText()
        title = soup.select("#wob_dc")[0].getText()
        humidity = soup.select("#wob_hm")[0].getText()
        time = soup.select("#wob_dts")[0].getText()
        wind = soup.select("#wob_ws")[0].getText()

        if str(responce) == str(f):
            logging.info('Подключение к серверам google прошло успешно ' + '(' + str(responce) + ')')
        else:
            logging.error('Поключение к серверам google прошло неудачно, не удалось подключится!' + '(' + str(responce) + ')', exc_info=True)

        talk(f"""\
дата и время: {time}
состояние: {title}
температура: {temperature}
влажность: {humidity}
ветер: {wind}
""")
    elif command in vk:
        talk('открываю вк')
        webbrowser.open('https://vk.com/feed')
    elif command in youtube:
        talk('открываю youtube')
        webbrowser.open('https://youtube.com/')
    elif command in telegram:
        talk('открываю телеграм')
        os.startfile('C:/Users/arcen/AppData/Roaming/Telegram Desktop/Telegram.exe')
    elif command in steam:
        talk('открываю steam')
        os.startfile('C:/Program Files (x86)/Steam/steam.exe')
    elif command in discord:
        talk('открываю discord')
        os.startfile('C:/Users/arcen/AppData/Local/Discord/Update.exe')

while True:
    archi()
