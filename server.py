from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Временное хранилище пользователей (можно заменить на базу данных)
users = {}


@app.route("/set_user/", methods=["POST"])
def set_user():
    data = request.json
    user_id = data.get("user_id")
    user_name = data.get("user_name")

    if not user_id or not user_name:
        return jsonify({"error": "Некорректные данные"}), 400

    users[user_id] = user_name
    logger.info(f"Пользователь {user_name} (ID: {user_id}) добавлен.")
    return jsonify({"message": f"Имя {user_name} сохранено!"})


@app.route("/get_user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify({"name": users[user_id]})
    return jsonify({"error": "Пользователь не найден"}), 404


@app.route("/")
def root():
    return jsonify({"message": "Сервер работает"})


@app.route("/health")
def health_check():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
