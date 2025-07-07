from flask import Flask, request
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

@app.route("/", methods=["POST"])
def send_alert():
    data = request.json
    msg = f"📡 NeuroX Alert:\n```{data}```"
    requests.post(WEBHOOK_URL, json={"content": msg})
    return "OK", 200

@app.route("/")
def home():
    return "NeuroX Discord Webhook is Live", 200
