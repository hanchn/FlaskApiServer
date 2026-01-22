from flask import render_template, request, redirect, url_for
from extensions import db
from models.user import User

def index():
    users = User.query.all()
    return render_template('index.html', users=users)

def add_user():
    username = request.form.get('username')
    email = request.form.get('email')
    if username and email:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('user.index'))
