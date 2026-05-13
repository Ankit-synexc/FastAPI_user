from fastapi import APIRouter
from models.user_schema import User
from Controller.user_controller import (
    get_all_users,
    get_single_user,
    create_new_user,
    update_existing_user,
    delete_existing_user
)
from services.user_services import *

router = APIRouter()


@router.get("/users")
def get_users():
    return get_all_users()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return get_single_user(user_id)


@router.post("/users")
    create_user( User)


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    return update_existing_user(user_id, updated_user)


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return delete_existing_user(user_id)
