from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()

# Assicura la directory persistente
os.makedirs("/data", exist_ok=True)
DB_PATH = "/data/repository.db"

# Crea il DB e la tabella se non esistono
conn = sqlite3.connect(DB_PATH)
conn.execute("""CREATE TABLE IF NOT EXISTS utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)""")
conn.commit()
conn.close()

@app.get("/")
def home():
    return {"msg": "API pronta"}

@app.get("/add/{nome}")
def add(nome: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO utenti (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()
    return {"msg": f"{nome} aggiunto"}

@app.get("/lista")
def lista():
    conn = sqlite3.connect(DB_PATH)
    utenti = conn.execute("SELECT * FROM utenti").fetchall()
    conn.close()
    return {"utenti": utenti}
#