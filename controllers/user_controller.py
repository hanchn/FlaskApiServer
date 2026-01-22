from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@user_bp.route('/add', methods=['POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')
    if username and email:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('user.index'))
