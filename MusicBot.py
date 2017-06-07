import time
import telepot
from apiclient.discovery import build
import argparse
import json

#Configurazione per interrogare le API di Google
DEVELOPER_KEY = "AIzaSyD7UmSpz9MUsk1FX0nCuz3Pfzkc9ffsSjY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

#Configurazione BOT
TOKEN='360912478:AAFFP864KdWdybNreoohQfyO-4u1C34O3io'
bot=telepot.Bot(TOKEN)

#Variabile globale utilizzata per la gestione dei comandi
commandOk=False


#Funzione che gestisce i messaggi inviati al BOT
def commands(msg):
    global commandOk
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        messaggio=msg['text']
        if messaggio == "/getSong":
            commandOk = True
        elif commandOk:
            song(messaggio, chat_id)
            commandOk = False
        else:
            bot.sendMessage(chat_id ,'Comandi disponibili: /getSong')
    else:
        bot.sendMessage(chat_id ,'Accetto solo messaggi di testo!')

#Funzione che prepara gli argomenti per le API di YT e invia il messaggio
def song(keys, chat_id):
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--q", help="Search term", default=keys)
    argparser.add_argument("--max-results", help="Max results", default=1)
    args = argparser.parse_args()
    youtube_search(args)
    videoID = youtube_search(args)
    bot.sendMessage(chat_id ,'https://www.youtube.com/watch?v='+videoID)

#Funzione che interroga le API di Google e ritorna le info del video più popolare
def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    risposta = json.dumps(search_response)
    risposta=json.loads(risposta)

    return risposta['items'][0]['id']['videoId']

#Programma principale
if __name__ == "__main__":
    
    bot.getUpdates()
    bot.message_loop(commands)

#Mantiene il programma in esecuzione
while 1:
    time.sleep(10)
