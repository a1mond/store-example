from models.user import UserModel
from werkzeug.security import hmac


def auth(username, password):
    user: UserModel = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user
    return None


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
