"""
uselessStats API v0.6

Scope:
- einfache FastAPI Anwendung
- persistente Speicherung von Tages Uptime
- SQLite als leichtgewichtige Datenbank
- Fokus auf Lernen und Nachvollziehbarkeit
- Funktionen besser verstehen, Syntax lernen
- Begleitete Entwicklung mit Code Reviews

Bewusste Entscheidungen:
- nicht alles an Code selbstschreiben aber verstehen
- keine Uhrzeiten gespeichert, um Verhaltensmetriken zu vermeiden
"""

from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager
from contextlib import contextmanager
from dotenv import load_dotenv
import os
import sqlite3

# Token laden aus Datei
load_dotenv(dotenv_path="./useless_token.env")
API_TOKEN = os.getenv("API_TOKEN")

# SQLite Datenbank
# liegt bewusst im /data Verzeichnis um Code und Daten zu trennen
# geeignet fürs Lernen und lokale Nutzung
DB_PATH = "./data/stats.sqlite"

# Token Check Funktion im Header
def check_token(authorization: str = Header(...)):
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Invalid or missing token")



# Datenbank Initialisierung
# Prüfung ob Tabelle "uptime" existiert, wenn nicht, wird sie erstellt
# Shutdown-Teil aktuell ungenutzt
@asynccontextmanager
async def lifespan(app: FastAPI):
    def init_db():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS uptime (
                id INTEGER PRIMARY KEY,
                day TEXT,
                uptime_seconds INTEGER
            )
        """)
        conn.commit()
        conn.close()

    # Funktionsaufruf
    init_db()

    # Ende des Startup Vorgangs
    yield

Version = "v0.6"
app = FastAPI(
    title="uselessStats api",
    version=Version,
    lifespan=lifespan
)

# Connection Handling via Context Manager
# sorgt für automatische Öffnung und Schließung der Verbindung
@contextmanager
def get_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
    finally:
        if conn:
            conn.close()

@app.get("/")
def root():
    return {"status": "ok", "message": f"uselessStats api {Version}"}

# GET /uptime
# Gibt alle gespeicherten Uptime Einträge zurück
# Leere Liste ist ein valider Zustand

@app.get("/uptime")
def get_uptime():
    with get_db() as conn:
        cursor = conn.cursor()

        # Tabelle uptime
        # uptime_seconds: gesamte On Zeit eines Tages in Sekunden
        # geholt wird die Gesamtsumme aller Uptime Einträge

        cursor.execute("SELECT SUM(uptime_seconds) FROM uptime")
        result = cursor.fetchone()

        return {"uptime_seconds": result[0] or 0}

class UptimeIn(BaseModel):

    uptime_seconds: int
    day: str

# POST /uptime
# schreibt Uptime Daten in die Datenbank und vorheriger Token Prüfung
# hartkodierter Endpoint ist erwünscht für einfachere Kontrolle

@app.post("/uptime")
def post_uptime(data: UptimeIn, token_check: None = Depends(check_token)):
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO uptime (uptime_seconds, day) VALUES (?, ?)",
            (data.uptime_seconds, data.day)
        )

        conn.commit()

        return {
            "status": "ok",
            "message": "uptime stored"
        }

## Roadmap – uselessStats API
#
### v0.3 [x]
# - FastAPI Basis
# - SQLite Speicherung
# - GET und POST Endpoint
#
### v0.4 [x]
# - ISO Datumsformat
# - POST addiert Uptime pro Tag
# - GET liefert Gesamtsumme aller uptime_seconds
#
### v0.5 [x]
# - automatische DB Initialisierung
# - sauberes Connection Handling
#
### v0.6 [x]
# - Bearer Token für GET und POST
#
### v0.7 [ ]
# - definiertes Fehlerverhalten
#
### v0.8 [ ]
# - Container Build
# - persistente SQLite Daten
#
### v0.9 [ ]
# - statische HTML Seite
# - Anzeige des Gesamtsumme
#
### v1.0 [ ]
# - vollständiges lauffähiges Produkt
#
### Future Ideas uselessStats API
#
# Glossar einbauen für z.B. IT Begriffe
# zurückgelegte Mausmeter
#