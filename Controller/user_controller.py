from models.user_schema import User
from services import user_services
from utils.response_util import success_response

def get_all_users():
    users = user_services.get_all_users()
    return success_response(data=users, message="All users fetched")

def get_single_user(user_id: int):
    user = user_services.get_user_by_id(user_id)
    if user:
        return success_response(data=user, message="User found")
    return success_response(data=None, message="User not found")

def create_new_user(user: User):
    created_user = user_services.create_user(user)
    return success_response(data=created_user, message="User created")

def update_existing_user(user_id: int, updated_user: User):
    user = user_services.update_user(user_id, updated_user)
    if user:
        return success_response(data=user, message="User updated")
    return success_response(data=None, message="User not found")

def delete_existing_user(user_id: int):
    success = user_services.delete_user(user_id)
    if success:
        return success_response(data=None, message="User deleted")
    return success_response(data=None, message="User not found")