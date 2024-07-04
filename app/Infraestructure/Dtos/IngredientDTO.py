from pydantic import UUID4, BaseModel


class IngredientDTO(BaseModel):
    name: str
    amount: int


class IngredientUpdateDTO(BaseModel):
    id: UUID4
    name: str
    amount: int
