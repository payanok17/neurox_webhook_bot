from flask import Flask, request
import telebot
import os
API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def webhook():
    return 'NeuroX Online'

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://neurox-webhook-bot.onrender.com/' + API_TOKEN)
    app.run(host='0.0.0.0', port=5000)
