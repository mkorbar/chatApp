from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, unique=False)
    message = db.Column(db.String, unique=False)


db.create_all()


@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)


@app.route('/send-message', methods=['POST'])
def save_message():
    username = request.form.get('username')
    message = request.form.get('message')

    msg = Message(author=username, message=message)
    db.session.add(msg)
    db.session.commit()

    print(f"User {username} send the following message: '{message}'")
    return redirect('/')


if __name__ == '__main__':
    app.run()
