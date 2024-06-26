from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient

class Dish_Factory:
    def __init__(self) -> None:
        pass
        

    def create(self, idPO:str, name:str, description:str, price:float, recipe:tuple[list[tuple[int, int]],str]) -> Dish:
        idVO = Id_Dish(idPO)
        nameVO = Name_Dish(name)
        descriptionVO = Description_Dish(description)
        priceVO = Price_Dish(price)
        recipeVO = None
        if (recipe is not None):
            ingridients_list:list[tuple[Id_Ingredient, int]] = []
        
            for ingridient in recipe[0]:
                ingridients_list.append((Id_Ingredient(ingridient[0]), ingridient[1]))
            recipeVO = Recipe(ingridients_list,recipe[1]) 

        return Dish(idVO, nameVO, descriptionVO, priceVO, recipeVO)
    
    def createId(self,idPO:str)->Id_Dish:
        return Id_Dish(idPO)