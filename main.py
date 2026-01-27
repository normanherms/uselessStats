"""
uselessStats API v0.4

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

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

Version = "v0.4"
app = FastAPI(
    title="useless stats api",
    version=Version
)


# SQLite Datenbank
# Liegt bewusst im data Verzeichnis um Code und Daten zu trennen
# Geeignet für Alpha und lokale Nutzung

DB_PATH = "data/stats.sqlite"


def get_db():
    return sqlite3.connect(DB_PATH)


@app.get("/")
def root():
    return {"status": "ok", "message": f"useless stats api {Version}"}

# GET /uptime
# Gibt alle gespeicherten Uptime Einträge zurück
# Leere Liste ist ein valider Zustand

@app.get("/uptime")
def get_uptime():
    conn = get_db()
    cursor = conn.cursor()

    # Tabelle uptime
    # uptime_seconds: gesamte On Zeit eines Tages in Sekunden
    # geholt wird die Gesamtsumme aller Uptime Einträge

    cursor.execute("SELECT SUM(uptime_seconds) FROM uptime")
    result = cursor.fetchone()

    conn.close()

    return {"uptime_seconds": result[0] or 0}

class UptimeIn(BaseModel):

    uptime_seconds: int
    day: str

# POST /uptime
# schreibt Uptime Daten in die Datenbank
# hartkodierter Endpoint ist erwünscht für einfachere Kontrolle

@app.post("/uptime")
def post_uptime(data: UptimeIn):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO uptime (uptime_seconds, day) VALUES (?, ?)",
        (data.uptime_seconds, data.day)
    )

    conn.commit()
    conn.close()

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
### v0.5 [ ]
# - automatische DB Initialisierung
# - sauberes Connection Handling
#
### v0.6 [ ]
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