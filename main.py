"""
uselessStats API v0.3

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
- keine Authentifizierung
"""

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

Version = "v0.3"
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
    # id: technische ID
    # uptime_seconds: gesamte On Zeit eines Tages in Sekunden
    # day: Datum ohne Uhrzeit um keine Nutzungsprofile zu erzeugen

    cursor.execute("SELECT id, uptime_seconds, day FROM uptime")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": row[0],
            "uptime_seconds": row[1],
            "day": row[2]
        }
        for row in rows
    ]


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

# To-Do (v0.3)
# - Authentifizierung hinzufügen mit Bearer Token
# - systemd oneshot service beim Shutdown