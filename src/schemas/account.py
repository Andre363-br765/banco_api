from pydantic import BaseModel, PositiveFloat

class AccountIn(BaseModel):
    user_id: int
    balance: PositiveFloat  # garante que saldo inicial não seja negativo
