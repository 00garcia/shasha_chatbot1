from flask import Flask, render_template, request, jsonify
from bot_logic import get_bot_response
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave_development")

# Configurar MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["shasha_db"]
collection = db["conversaciones"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    session_id = request.json.get("session_id")

    conv = collection.find_one({"session_id": session_id})
    if not conv:
        user_data = {}
    else:
        user_data = conv.get("user_data", {})

    resp, nuevos_datos, finished = get_bot_response(user_msg, user_data)

    user_data.update(nuevos_datos)

    collection.update_one(
        {"session_id": session_id},
        {"$set": {"user_data": user_data, "last_message": user_msg}},
        upsert=True
    )

    return jsonify({"response": resp, "user_data": user_data, "finished": finished})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
