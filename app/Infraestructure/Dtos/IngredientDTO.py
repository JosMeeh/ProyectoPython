from pydantic import BaseModel


class IngredientDTO(BaseModel):
    name: str
    amount: int
