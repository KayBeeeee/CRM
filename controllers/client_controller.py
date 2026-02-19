from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Client, Contact
from services.client_code_generator import generate_client_code

client_bp = Blueprint('clients', __name__, template_folder='../templates/clients')

@client_bp.route('/')
def list_clients():
    clients = Client.query.order_by(Client.name.asc()).all()
    return render_template('list_clients.html', clients=clients)

@client_bp.route('/new', methods=['GET', 'POST'])
def create_client():
    if request.method == 'POST':
        name = request.form.get('name')
        additional_info = request.form.get('additional_info')
        if not name:
            flash("Name is required", "error")
            return redirect(url_for('clients.create_client'))
        client = Client(name=name, additional_info=additional_info)
        db.session.add(client)
        db.session.flush()  # get ID for code generation
        client.client_code = generate_client_code(name, db.session, Client)
        db.session.commit()
        return redirect(url_for('clients.list_clients'))
    return render_template('create_client.html')
