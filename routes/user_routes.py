from flask import Blueprint
from controllers import user_controller

user_bp = Blueprint('user', __name__)

user_bp.route('/', methods=['GET'])(user_controller.index)
user_bp.route('/add', methods=['POST'])(user_controller.add_user)
