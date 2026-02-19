from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models.contact import Contact

contact_bp = Blueprint("contacts", __name__, url_prefix="/contacts")


@contact_bp.route("/")
def list_contacts():
    contacts = Contact.query.order_by(Contact.surname.asc(), Contact.name.asc()).all()
    return render_template("contacts/list.html", contacts=contacts)


@contact_bp.route("/create", methods=["GET", "POST"])
def create_contact():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]

        if not name or not surname or not email:
            return render_template("contacts/form.html", error="All fields required")

        if Contact.query.filter_by(email=email).first():
            return render_template("contacts/form.html", error="Email must be unique")

        contact = Contact(name=name, surname=surname, email=email)
        db.session.add(contact)
        db.session.commit()

        return redirect(url_for("contacts.list_contacts"))

    return render_template("contacts/form.html")
