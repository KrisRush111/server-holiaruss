from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Временное хранилище пользователей (можно заменить на базу данных)
users = {}

@app.route('/set_user', methods=['POST'])
def set_user():
    data = request.get_json()
    user_id = data.get("user_id")
    user_name = data.get("user_name")
    if user_id and user_name:
        users[user_id] = user_name
        logger.info(f"Пользователь {user_name} (ID: {user_id}) добавлен.")
        return jsonify({"message": f"Имя {user_name} сохранено!"}), 200
    return jsonify({"error": "Некорректные данные"}), 400

@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify({"name": users[user_id]}), 200
    return jsonify({"error": "Пользователь не найден"}), 404

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "Сервер работает"}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
