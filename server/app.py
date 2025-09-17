from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# initialize app
app = Flask(__name__)
CORS(app)  # allow React frontend to access Flask API

# database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import models AFTER db init
from models import Message

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([m.to_dict() for m in messages])

@app.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    new_msg = Message(username=data['username'], body=data['body'])
    db.session.add(new_msg)
    db.session.commit()
    return jsonify(new_msg.to_dict()), 201

@app.route('/messages/<int:id>', methods=['PATCH'])
def update_message(id):
    message = Message.query.get_or_404(id)
    data = request.get_json()
    if "body" in data:
        message.body = data["body"]
    db.session.commit()
    return jsonify(message.to_dict())

@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    return '', 204


if __name__ == "__main__":
    app.run(port=5555, debug=True)
