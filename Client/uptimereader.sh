#!/bin/bash

# Kleines uptime Reader Script mit curl aufruf zum POST Endpoint der useless Stats API
# Liest Uptime in Sec aus und Datum im Format DD.MM.YYYY und schreibt es in eine Variable
# Variable wird beim curl Aufruf wieder ausgelesen und gesetzt
# Script ausführbar machen mit chmod +x ./uptimereader.sh, starten mit ./uptimereader.sh

UPTIME=$(awk '{print int($1)}' /proc/uptime)
DAY=$(date +%d.%m.%Y)

curl -X POST "http://127.0.0.1:8000/uptime" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d "{\"uptime_seconds\": $UPTIME, \"day\": \"$DAY\"}"
