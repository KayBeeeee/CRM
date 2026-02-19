from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from models.client import Client
from models.contact import Contact
from services.client_code_generator import generate_client_code

client_bp = Blueprint("clients", __name__, url_prefix="/clients")


@client_bp.route("/")
def list_clients():
    clients = Client.query.order_by(Client.name.asc()).all()
    return render_template("clients/list.html", clients=clients)


@client_bp.route("/create", methods=["GET", "POST"])
def create_client():
    if request.method == "POST":
        name = request.form["name"]

        if not name:
            return render_template("clients/form.html", error="Name is required")

        code = generate_client_code(name)

        client = Client(name=name, client_code=code)
        db.session.add(client)
        db.session.commit()

        return redirect(url_for("clients.edit_client", client_id=client.id))

    return render_template("clients/form.html")


@client_bp.route("/<int:client_id>", methods=["GET"])
def edit_client(client_id):
    client = Client.query.get_or_404(client_id)
    contacts = Contact.query.order_by(Contact.surname.asc()).all()
    return render_template("clients/form.html", client=client, contacts=contacts)


@client_bp.route("/<int:client_id>/link", methods=["POST"])
def link_contact(client_id):
    client = Client.query.get_or_404(client_id)
    contact_id = request.json.get("contact_id")

    contact = Contact.query.get(contact_id)

    if contact not in client.contacts:
        client.contacts.append(contact)
        db.session.commit()

    return jsonify({"status": "linked"})
