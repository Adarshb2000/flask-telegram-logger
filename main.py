import os
from flask import Flask, request
from flask_cors import CORS
from telegram import Bot

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
USER_ID = os.environ["USER_ID"]

app = Flask(__name__)
CORS(app)
bot = Bot(TELEGRAM_TOKEN)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/update", methods=["POST"])
async def update():
    data = request.get_json()
    message = data["message"]

    async with bot:
        await bot.send_message(chat_id=USER_ID, text=message)

    return "Hello World!"


if __name__ == "__main__":
    app.run("0.0.0.0", 8353)
