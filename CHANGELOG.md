# Changelog

### 28.01.2026
  - Datenbank Initialisierung eingefügt per @asynccontextmanager (lifespan)
  - Connection Handling per @contextmanager umgesetzt für stabilere Verbindungen in API Endpoints
### 27.01.2026
  - ISO Datum in uptimereader.sh gesetzt sowie Doku erweitert, uptime.service Doku ergänzt
  - GET Endpoint **uptime** gibt nur noch die Gesamtsumme aller uptime_seconds zurück
  - Mehrere POSTs pro Tag möglich (werden einzeln gespeichert, bei GET summiert)
  - Repo Struktur in der Readme überarbeitet 
### 26.01.2026 
  - in main.py POST Funktion hinzugefügt, Client Script und Service hinzugefügt unter /Client 
### 25.01.2026 
  - main.py mit Basic Get Funktion erstellt für / und /uptime. 
### 25.01.2026
  - Projekt Start und init Commit, README.md geschrieben