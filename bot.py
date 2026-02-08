import time
import requests

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1470122751745331211/fCbvG65ipiY9__g8kSacoezblWyWNfKQIxMUKGNrwjVr9qnRhHIBfHyZROXMg3o7ENWV"

def send(msg):
    requests.post(DISCORD_WEBHOOK, json={"content": msg})

send("🟢 JP Hunter bot started")

while True:
    send("👀 Bot is alive and running")
    time.sleep(3600)
