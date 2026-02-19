from flask import Flask, render_template, request, jsonify
import sqlite3
from chatbot_logic import get_response

app = Flask(__name__)


def save_message(user_message, bot_response):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS chats (user TEXT, bot TEXT)")
    cursor.execute("INSERT INTO chats (user, bot) VALUES (?, ?)",
                   (user_message, bot_response))
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_response = get_response(user_message)
    save_message(user_message, bot_response)
    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
