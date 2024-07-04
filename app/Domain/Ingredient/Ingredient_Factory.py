from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient, Name_Ingredient, Amount_Ingredient

# Fabrica de Ingredientes
# Permite la creacion de un nuevo ingrediente
class Ingredient_Factory:
    def __init__(self) -> None:
        pass

    # Crea un ingrediente con todos sus atributos
    def create(self, idPO: str, name: str, amount: int) -> Ingredient:
        idVO = Id_Ingredient(idPO)
        nameVO = Name_Ingredient(name)
        amountVO = Amount_Ingredient(amount)

        return Ingredient(idVO, nameVO, amountVO)

    # Crea el id de un ingrediente
    def createId(self,idPO:str)->Id_Ingredient:
        return Id_Ingredient(idPO)
