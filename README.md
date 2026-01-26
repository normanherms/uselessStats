# Useless Stats

## Willkommen & Idee

Willkommen bei uselessStats, schön das du hergefunden hast.

Die Idee kam mir beim Betrachten der Helm Charts von OpenCloud. Es war schlicht zu viel um mal eben zu deployen, zu wenig weiß ich über 
Kubernetes und die Technologien die bei OpenCloud verwendet werden. Um nicht einfach mit Trail and Error weiterzumachen, überlegte ich mir diese Alternative.
Wir alle haben in unserem Leben unnütze Statistiken die uns aber vielleicht doch interessieren, wenn auch nur einmalig. Dinge die mir spontan einfielen waren zum 
Beispiel wie viel Sprit hat man getankt über den Monat, wie viele Schritte läuft man die Woche usw. Aber ich wollte keine simple Vergleichbarkeit. 
Also überlegte ich die Werte zu entkoppeln nicht wie viel Sprit, sondern wie viel Barrel Rohöl oder welche Strecke ist man gelaufen wie zum Beispiel von Hamburg nach Nussloch oder ähnliches.

Der erste init commit war am 25.01.2026

## Struktur des Repo's

[README.md](/README.md)                   # Dieses Dokument
[requirements.txt](/requirements.txt)     # Voraussetzungen zum Ausführen des Codes

## Zweck des Projekts

**Useless Stats** ist ein bewusst einfaches Lern- und Demo-Projekt mit einem klaren praktischen Ziel: ein vollständiger, realer **End-to-End-Use-Case** für meinen K3s-Cluster.

Am Ende steht **eine öffentlich erreichbare Webseite**, die auf dem eigenen K3s-Cluster läuft und persönliche, banale Statistiken darstellt.

Der Zweck ist **nicht** Selbstoptimierung, Vergleich oder Produktivität, sondern:

* Lernen von Fullstack-Grundlagen
* Verstehen von Datenfluss (Client → API → DB → Frontend)
* Aufbau eines realen, aber harmlosen Use-Cases
* Betrieb einer eigenen Anwendung im Cluster

---

## Lernziele

Das Projekt ist bewusst so gestaltet, dass folgende Themen praktisch gelernt werden:

### systemd Handling

* schreiben einer eigenen Servicedatei
* Ausführung vor poweroff.target 

### Bash

* einfache Zähler und Counter
* periodisches Senden von Daten
* grundlegende Fehlerbehandlung

### Backend (Python)

* einfache REST-API
* GET- und POST-Endpoints
* minimale Validierung
* klare Trennung von Logik und Daten

### Datenbank

* einfache Tabellen
* Inserts und Aggregation
* aktuell bewusster Verzicht auf Overhead

### Frontend

* statisches HTML
* leichtes CSS
* optional minimales JavaScript
* Anzeige statt Interaktion

### Container & Betrieb

* ein schlankes Container-Image
* Auslieferung über Nginx oder ähnlichen Minimal-Webserver
* Deployment auf K3s
* echter Service

---

## Ergebnis

Am Ende existiert:

* ein Container-Image
* das auf dem K3s-Cluster läuft
* eine statische Webseite ausliefert
* Daten aus einer eigenen API anzeigt

Das Projekt dient damit als **vollständiger, nachvollziehbarer Use-Case** für Entwicklung, Deployment und Betrieb.

---

## Designprinzipien

1. **Einfachheit**

   * wenige Frameworks
   * keine Magie
   * alles nachvollziehbar

2. **Geschwindigkeit**

   * schnelle Ladezeiten
   * einfache Queries
   * kein bewusstes Overengineering

3. **Sicherheit**

   * klare Trennung von API und Frontend
   * kein direkter Datenbankzugriff von außen
   * minimale Angriffsfläche

4. **Anfängerfreundlichkeit**

   * jedes Teil für sich verständlich
   * Fokus auf Grundlagen
   * Lernen durch Verstehen des Codes
   * Unterstützung von modernen Lernhilfen (ChatGPT)
   * nicht alles selbst schreiben am Anfang aber nachhaltig Verständnis aufbauen
   * im Verlauf das eigene weiterentwickeln lernen sowie Best Practises verstehen

---

## Architekturüberblick

```
[systemd oneshot Service]
    ↓ 
[Bash Script]
    ↓ POST
[Python API]
    ↓ SQLite
[Aggregation & Übersetzung]
    ↓ 
[Statisches Frontend]
    ↓
[Nginx Container]
    ↓
[K3s Cluster]
```

---

## Datenkonzept

### Rohdaten

Gespeichert werden ausschließlich einfache Events:

* Metrik-Name
* Wert

Beispiele bzw Ideen:

* Uptime
* Tastaturanschläge
* Bildschirmzeit
* Mausdistanz

Keine Nutzerprofile, keine Geräte-IDs, keine sensiblen Daten.

---

## Umrechnung und Darstellung

Rohdaten werden **nicht direkt** angezeigt.

Stattdessen erfolgt eine bewusste Umrechnung in **banales, nicht handlungsrelevantes Wissen**.

Beispiele:

* nicht „Stunden“, sondern „volle Tage“
* nicht „Kilometer“, sondern „von X nach Y“

Die Umrechnung erfolgt **serverseitig in der API**, nicht im Frontend.

---

## Frontend-Zielbild

Die Webseite ist bewusst ruhig und reduziert.

Beispiel:

```
═══════════════════════════════════════
   USELESS STATS V1.0
═══════════════════════════════════════

💻 COMPUTER USAGE
   Keyboard input:   42.384 strokes
   Translation:      ≈ 23 DIN-A4 pages

🖱 INPUT DEVICES
   Mouse distance:   3.2 km
   Translation:      ≈ once around the block

   SCREEN TIME
   Total time:       18h
   Translation:      ≈ almost one full day

═══════════════════════════════════════
```

Keine Ziele, keine Balken, keine Bewertung.

---

## Explizit nicht enthalten

* Gamification
* Zielvorgaben
* Rankings
* Vergleich mit anderen
* Health-Tracking
* Social-Features

---

## Projektphasen

### Phase 1 – Minimaler Use-Case

* Service Datei
* simples Bash Script
* eine Metrik
* eine API
* eine Sqlite Datenbank
* eine Anzeige

### Phase 2 – Erweiterung

* mehrere Metriken
* mehrere Umrechnungen

### Phase 3 – Betrieb

* Container-Build
* K3s-Deployment
* optional Monitoring

---

## Lokales Setup (PyCharm)

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

## Leitmotiv

> Das Projekt existiert um ein besseres Verständnis zu entwickeln wie Dinge zusammenhängen. 
> Weitere Learnings, systemd Service Dateien, Bash Scripting, Python und Fast API, Container Builds und Helm Charts.
> Vielleicht auch endlich das erste CI/CD Projekt.

**Letzte Änderung: 26.01.2026**
