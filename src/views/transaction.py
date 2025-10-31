from pydantic import BaseModel, AwareDatetime, NaiveDatetime, PositiveFloat

class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    timestamp: AwareDatetime | NaiveDatetime
