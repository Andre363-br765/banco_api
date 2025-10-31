from enum import Enum
from pydantic import BaseModel, PositiveFloat

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

class TransactionIn(BaseModel):
    account_id: int
    type: TransactionType
    amount: PositiveFloat  # garante que o valor seja positivo

    class Config:
        use_enum_values = True  # salva o enum como string no banco
