from ..models.user import UsersModel
from flask import Blueprint
import pdb

user_bp = Blueprint('user_bp', __name__)
# get users
@user_bp.route('/users', methods=["GET"])
def get_users():
    if request.method == 'GET':
        users = UsersModel.query.all()
        results = [
            {
                'name': user.name
            }for user in users]
    return jsonify(results)