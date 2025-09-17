from app import db

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "body": self.body
        }
