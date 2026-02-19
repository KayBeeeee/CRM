from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Contact, Client

contact_bp = Blueprint('contacts', __name__, template_folder='../templates/contacts')

@contact_bp.route('/')
def list_contacts():
    contacts = Contact.query.order_by(Contact.surname.asc(), Contact.name.asc()).all()
    return render_template('list_contacts.html', contacts=contacts)

@contact_bp.route('/new', methods=['GET', 'POST'])
def create_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        if not (name and surname and email):
            flash("All fields are required", "error")
            return redirect(url_for('contacts.create_contact'))
        existing = Contact.query.filter_by(email=email).first()
        if existing:
            flash("Email must be unique", "error")
            return redirect(url_for('contacts.create_contact'))
        contact = Contact(name=name, surname=surname, email=email)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contacts.list_contacts'))
    clients = Client.query.order_by(Client.name.asc()).all()
    return render_template('create_contact.html', clients=clients)
