from app import db

client_contact = db.Table(
    "client_contact",
    db.Column("client_id", db.Integer, db.ForeignKey("client.id"), primary_key=True),
    db.Column("contact_id", db.Integer, db.ForeignKey("contact.id"), primary_key=True)
)
