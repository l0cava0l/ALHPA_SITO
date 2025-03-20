import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    """
    Inizializza il database se non esiste
    Crea la tabella degli utenti
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def verify_user(email, password):
    """
    Verifica le credenziali utente nel database
    argomenti:
        email (str): Email dell'utente
        password (str): Password da verificare
    ritorno: True se le credenziali sono valide, False altrimenti(booleano)
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user[1], password):
        return True
    return False

def check_email_exists(email):
    """
    Verifica se un'email è già registrata nel database
    Aagomenti: email (str): Email da verificare
    ritorno: True se l'email esiste, False altrimenti(boolenao)
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
    existing_user = cursor.fetchone()
    conn.close()
    
    return existing_user is not None

def create_user(email, password):
    """
    Crea un nuovo utente nel database
    argomenti:
        email (str): Email del nuovo utente
        password (str): Password da hashare e salvare
    ritorno: True se l'utente è stato creato con successo, False altrimenti(boolenao)
    """
    if check_email_exists(email):
        return False
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
    conn.commit()
    conn.close()
    
    return True