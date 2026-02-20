# controllers/client_controller.py
from flask import Blueprint, request, jsonify
from models import db, Client

client_bp = Blueprint("client_bp", __name__)

@client_bp.route("/", methods=["GET"])
def list_clients():
    clients = Client.query.order_by(Client.name.asc()).all()
    if not clients:
        return jsonify({"message": "No client(s) found."}), 200
    data = []
    for c in clients:
        data.append({
            "name": c.name,
            "client_code": c.client_code,
            "num_contacts": len(c.contacts)
        })
    return jsonify(data)
