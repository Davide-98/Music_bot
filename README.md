Music_bot

MusicBot è un bot di Telegram programmato per permettere all'utente di guardare il video della canzone che si sta cercando.

E' in grado di inviare un messaggio contenente l'URL del video di YouTube a partire da una serie di parole chiave inviate al bot 
(es. il titolo della canzone). E' possibile fare ciò attraverso il comando /getSong.

Per provare questi codici sarà necessario installare Python3 sul proprio computer e aggiungere delle librerie python:

    - Telepot, libreria di telegram. COMANDO: pip install telepot
    
    - la libreria di Google per utilizzare le sue API. COMANDO: pip install google-api-python-client

Per aggiungere il bot a Telegram basta cercare "@TESINA_MUSIC_bot" nella barra di ricerca di Telegram e avviarlo.

PROGRAMMI:

Funzionante.py => programma funzionante che ritorna il video della canzone che si sta cercando, però senza l'uso del comando /getSong

Prova.py => programma dove si effettuano delle prove per ovviare al problema delle due letture che si presenta se si vuole utilizzare il comando /getSong

ProvaDueLetture.py => prova fatta per risolvere il problema delle due letture incapsulando una nell'altra. Presenta problemi.
