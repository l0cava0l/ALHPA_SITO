from flask import Flask, render_template, request, redirect, url_for, make_response
import secrets
from AlphaBot import AlphaBot
import db_config

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
bot = AlphaBot()
db_config.init_db() #inizializza db

def is_authenticated(request):
    """
    Verifica se l'utente è autenticato:
        argomenti: L'oggetto request della richiesta HTTP(request)
        ritorno: (autenticato, email)
    """
    token = request.cookies.get('auth_token')
    email = request.cookies.get('user_email')
    
    if not token or not email:
        return False, None
    return True, email

@app.route("/", methods=["GET"])
def home():
    """
    Gestisce la pagina principale
    Reindirizza alla home se autenticato, altrimenti alla pagina di login
    """
    authenticated, email = is_authenticated(request)
    if authenticated:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))
    

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Gestisce la pagina di login
    GET: Mostra il form di login
    POST: Processa i dati di login
    """
    if request.method == "POST":
        email = request.form.get('e-mail')
        password = request.form.get('password')
        
        # Verifica le credenziali utilizzando il modulo db_config
        if db_config.verify_user(email, password):
            # Creazione token di autenticazione
            token = secrets.token_hex(16)
            # Creazione della risposta e imposta i cookie
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('auth_token', token, httponly=True)
            response.set_cookie('user_email', email, httponly=True)
            
            return response
        else:
            # errore credenziali 
            return render_template('login.html', error="Credenziali non valide")
    
    #mostra la pagina di login (GET)
    return render_template('login.html')

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    """
    Gestisce la creazione di un nuovo account
    GET: Mostra il form di creazione account
    POST: Processa i dati per creare un nuovo account
    """
    if request.method == "POST":
        email = request.form.get('e-mail')
        password = request.form.get('password')
        
        # crearezione di un nuovo utente
        if db_config.create_user(email, password):
            # Reindirizza alla pagina di login (rifare accesso)
            return redirect(url_for('login'))
        else:
            return render_template('create_account.html', error="Email già in uso")
    
    #mostra la pagina di creazione account(GET)
    return render_template('create_account.html')

@app.route("/dashboard")
def dashboard():
    """
    Mostra la dashboard utente dopo il login
    """
    authenticated, email = is_authenticated(request)
    if not authenticated:
        return redirect(url_for('login'))
    return render_template('home.html', username=email)

@app.route("/control")
def control():
    """
    Mostra la pagina di controllo dell'AlphaBot
    """
    authenticated, email = is_authenticated(request)
    if not authenticated:
        return redirect(url_for('login'))
    return render_template('control.html', username=email)

@app.route("/logout")
def logout():
    """
    Gestisce il logout dell'utente
    """
    # risposta di reindirrizamento al login
    response = make_response(redirect(url_for('login')))
    # Eliminazione  dei cookie di autenticazione
    response.delete_cookie('auth_token')
    response.delete_cookie('user_email')
    return response

#controllo dell'AlphaBot
@app.route("/move/forward")
def move_forward():
    """
    Fa muovere l'AlphaBot in avanti
    """
    authenticated, _ = is_authenticated(request)
    if not authenticated:
        return redirect(url_for('login'))
    bot.forward()
    return redirect(url_for('control'))

@app.route("/move/backward")
def move_backward():
    """
    Fa muovere l'AlphaBot indietro
    """
    authenticated, _ = is_authenticated(request)
    if not authenticated:
        return redirect(url_for('login'))
    bot.backward()
    return redirect(url_for('control'))

@app.route("/move/left")
def move_left():
    """
    Fa ruotare l'AlphaBot a sinistra
    """
    authenticated, _ = is_authenticated(request)
    if not authenticated:
        return redirect(url_for('login'))
    bot.left()
    return redirect(url_for('control'))

@app.route("/move/right")
def move_right():
    """
    Fa ruotare l'AlphaBot a destra
    """
    authenticated, _ = is_authenticated(request)
    if not authenticated:
        return redirect(url_for('login'))
    bot.right()
    return redirect(url_for('control'))

@app.route("/move/stop")
def move_stop():
    """
    Ferma l'AlphaBot
    """
    authenticated, _ = is_authenticated(request)
    if not authenticated:
        return redirect(url_for('login'))
    bot.stop()
    return redirect(url_for('control'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4444)