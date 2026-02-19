from app import db
from models.association import client_contact

class Client(db.Model):
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    client_code = db.Column(db.String(6), unique=True, index=True)

    contacts = db.relationship(
        "Contact",
        secondary=client_contact,
        back_populates="clients"
    )
