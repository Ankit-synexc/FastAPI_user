import re
from fastapi import HTTPException
from models.user_schema import User


def validate_user_data(user: User):
    if not user.name or len(user.name.strip()) < 2:
        raise HTTPException(
            status_code=400,
            detail="Name cannot be empty and must be at least 2 characters long."
        )
    if user.number <= 0:
        raise HTTPException(
            status_code=400,
            detail="Phone number must be a positive integer."
        )

    if len(str(user.number)) < 10:
        raise HTTPException(
            status_code=400,
            detail="Phone number must contain at least 10 digits."
        )
    if type(user.name) is not str:
        raise HTTPException(
            status_code=400,
            detail="Name must be a string."
        )
    if type(user.id) is not int:
        raise HTTPException(
            status_code=400,
            detail="ID must be a integer."
        )