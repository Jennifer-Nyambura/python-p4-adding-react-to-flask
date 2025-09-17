from app import app, db
from models import Message

with app.app_context():
    db.drop_all()
    db.create_all()

    msg1 = Message(username="Alice", body="Hello from Flask!")
    msg2 = Message(username="Bob", body="React + Flask works!")

    db.session.add_all([msg1, msg2])
    db.session.commit()

    print("✅ Database seeded!")
