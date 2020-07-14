from .users_controller import user_bp

def init_app(app):
    app.register_blueprint(user_bp)




# from flask import Blueprint, request, jsonify
# from models.user import UsersModel

# def get_users():
#     if request.method == 'GET':
#         users = UsersModel.query.all()
#         results = [
#             {
#                 'name': user.name
#             }for user in users]
#     return jsonify(results)