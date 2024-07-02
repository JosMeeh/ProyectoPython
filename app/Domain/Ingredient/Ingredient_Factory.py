from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient, Name_Ingredient, Amount_Ingredient


class Ingredient_Factory:
    def __init__(self) -> None:
        pass

    def create(self, idPO: str, name: str, amount: int) -> Ingredient:
        idVO = Id_Ingredient(idPO)
        nameVO = Name_Ingredient(name)
        amountVO = Amount_Ingredient(amount)

        return Ingredient(idVO, nameVO, amountVO)
