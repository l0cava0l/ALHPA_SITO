AlphaBot - Flask Login System

Descrizione del progetto

AlphaBot è un progetto scolastico basato su Flask che permette di controllare il movimento di un AlphaBot tramite un'interfaccia web. Il sistema include autenticazione degli utenti, gestione delle sessioni e interazione con un database, consentendo agli utenti di accedere e controllare il robot tramite un sito web.

Struttura del progetto

baseLogin-main/
  baseLogin-main/
    AlphaBot.py
    app.py
    db_config.py
    static/
      style.css
    templates/
      control.html
      create_account.html
      home.html
      login.html
    __pycache__/  (file compilati da Python)

app.py: File principale che gestisce l'applicazione Flask.

AlphaBot.py: Modulo responsabile del controllo e movimento dell'AlphaBot.

db_config.py: Gestione della configurazione del database.

static/: Contiene file statici come CSS.

templates/: Contiene i file HTML per il rendering delle pagine web.

Dettaglio di app.py

Il file app.py contiene le seguenti funzionalità principali:

Inizializzazione dell'app Flask

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

Viene creata l'applicazione Flask con una secret_key casuale per la gestione delle sessioni.

Inizializzazione del database

db_config.init_db()

Viene chiamata la funzione di inizializzazione del database definita in db_config.py.

Funzione di autenticazione

def is_authenticated(request):
    token = request.cookies.get('auth_token')
    email = request.cookies.get('user_email')
    if not token or not email:
        return False, None
    return True, email

Questa funzione verifica se un utente è autenticato controllando la presenza di un token nei cookie.

Rotte principali

Home (/): Reindirizza alla dashboard se l'utente è autenticato, altrimenti alla pagina di login.

Login (/login): Gestisce il login dell'utente.

Control (/control): Pagina in cui gli utenti autenticati possono inviare comandi di movimento all'AlphaBot.

@app.route("/", methods=["GET"])
def home():
    authenticated, email = is_authenticated(request)
    if authenticated:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

Installazione

Clona il repository:

git clone https://github.com/tuo-utente/AlphaBot.git

Entra nella cartella del progetto:

cd AlphaBot

Installa le dipendenze:

pip install -r requirements.txt

Avvia il server Flask:

python app.py

Utilizzo

Apri il browser e vai su http://127.0.0.1:5000/

Segui le istruzioni per creare un account o effettuare il login.

Una volta autenticato, accedi alla pagina di controllo per inviare comandi di movimento all'AlphaBot.
