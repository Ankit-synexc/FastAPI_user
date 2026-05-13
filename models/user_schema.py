from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id: int
    name: str = Field(min_length=2)
    email: EmailStr
    number: int = Field(ge=1000000000) # Ensures at least 10 digits