from ..models.user import UsersModel
# get users
@app.route('/users', methods=["GET"])
def get_users():
    if request.method == 'GET':
        users = UsersModel.query.all()
        results = [
            {
                'name': user.name
            }for user in users]
    return jsonify(results)