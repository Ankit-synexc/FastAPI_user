from Controller.user_controller import *


def get_user(user_id: int):
    return get_single_user(user_id)



def create_user(user: User):
    return create_new_user(user)

def update_user(user_id: int, updated_user: User):
    return update_existing_user(user_id, updated_user)

def delete_user(user_id: int):
    return delete_existing_user(user_id)