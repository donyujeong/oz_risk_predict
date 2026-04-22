from datetime import datetime
from pydantic import BaseModel

# 회원가입 응답의 구조
class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime