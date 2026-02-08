import time
import requests

DISCORD_WEBHOOK = "WKLEJ_TUTAJ_WEBHOOK"

def send(msg):
    requests.post(DISCORD_WEBHOOK, json={"content": msg})

send("🟢 JP Hunter bot started")

while True:
    send("👀 Bot is alive and running")
    time.sleep(3600)
