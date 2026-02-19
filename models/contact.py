from app import db
from models.association import client_contact

class Contact(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)

    clients = db.relationship(
        "Client",
        secondary=client_contact,
        back_populates="contacts"
    )
