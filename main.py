"""
uselessStats API v0.1

Scope:
- einfache FastAPI Anwendung
- persistente Speicherung von Tages Uptime
- SQLite als leichtgewichtige Datenbank
- Fokus auf Lernen und Nachvollziehbarkeit

Bewusste Entscheidungen:
- keine Uhrzeiten gespeichert, um Verhaltensmetriken zu vermeiden
- keine Authentifizierung
"""

from fastapi import FastAPI
import sqlite3

app = FastAPI()

# SQLite Datenbank
# Liegt bewusst im data Verzeichnis um Code und Daten zu trennen
# Geeignet für v0.1 und lokale Nutzung

DB_PATH = "data/stats.sqlite"


def get_db():
    return sqlite3.connect(DB_PATH)


@app.get("/")
def root():
    return {"status": "ok", "message": "useless stats api v0.1"}

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

# To-Do (v0.2)
# - POST Endpoint zum automatischen Eintragen
# - systemd oneshot beim Shutdown