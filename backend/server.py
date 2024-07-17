from flask import Flask, jsonify, request
from backend.langgraph_agent import MasterAgent

backend_app = Flask(__name__)

@backend_app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Running"}), 200

@backend_app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.json
    master_agent = MasterAgent()
    quiz = master_agent.run(data["topics"], data["layout"])
    return jsonify({"path": quiz}), 200

