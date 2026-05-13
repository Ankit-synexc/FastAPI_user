from fastapi import APIRouter
from models.user_schema import User
import controller.user_controller as controller

router = APIRouter()

@router.get("/users")
def get_users():
    return controller.get_all_users()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return controller.get_single_user(user_id)

@router.post("/users")
def create_user(user: User):
    return controller.create_new_user(user)

@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    return controller.update_existing_user(user_id, updated_user)

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return controller.delete_existing_user(user_id)