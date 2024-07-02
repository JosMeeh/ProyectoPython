from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository


class Update_Dish_Parameter(IService_Parameter):
    def __init__(self, id:str, name:str, description:str, price:float, recipe:tuple[list[tuple[int, int]],str]) -> None:
        super().__init__(Service_Type.Command_Update)
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe


class Update_Dish_Response(IService_Response):
    def __init__(self,id:str, name:str, description:str, price:float, recipe:tuple[list[tuple[str, int]],str]) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe

""" 

"""
class Update_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository, food_repository:Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Dish_Factory()

    async def execute(self, servicePO: Update_Dish_Parameter) -> IService_Response:
        new_dish = self.__factory.create(
            servicePO.id,
            servicePO.name,
            servicePO.description,
            servicePO.price,
            servicePO.recipe
        )

        updated_dish:Dish | None | Exception = await self.__repository.updateDish(
            new_dish.getId(),
            new_dish.name,
            new_dish.description,
            new_dish.price,
            new_dish.recipe
        )
        if isinstance(updated_dish,Exception):
            return Error_Response(updated_dish)
        if updated_dish is None:
            return NotFound_Response()
        
        #CREAR RESPONSE
        response = Update_Dish_Parameter(
            updated_dish.getId().id,
            updated_dish.name.name,
            updated_dish.description.description,
            updated_dish.price.price,
            None
        )
        
        #Buscar Ingredientes
        if updated_dish.recipe is not None:
            ingredient_list:list[tuple[str, int]] = []
            for i in updated_dish.recipe.ingredients:
                ingredient:Ingredient | Exception = await self.__foodrepository.searchIngredientbyId(i[0])
                if not isinstance(ingredient,Exception):
                    ingredient_list.append((ingredient.name_Ingredient.name, i[1]))
            response.recipe = (ingredient_list, updated_dish.recipe.instructions)

        return response
