from models.user_schema import User

# Simulated Database
users_db = []

def get_all_users_query():
    return users_db

def get_user_by_id_query(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return None

def create_user_query(user: User):
    users_db.append(user)
    return user

def update_user_query(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    return None

def delete_user_query(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return True
    return False