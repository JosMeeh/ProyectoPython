from __future__ import annotations

from app.Application.Dish.Query.Service_Dish_ById import SearchById_Dish_Response
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient import Ingredient


class SearchAll_Dish_Parameter(IService_Parameter):
    def __init__(self) -> None:
        super().__init__(Service_Type.Query_all)
        self.id = id


class SearchAll_Dish_Response(IService_Response):
    def __init__(self, dishes:list[SearchById_Dish_Response]) -> None:
        super().__init__(Result_Type.Result)
        self.dishes = dishes


""" 

"""
class SearchAll_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository, food_repository:Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Dish_Factory()

    async def execute(self, servicePO: SearchAll_Dish_Parameter) -> IService_Response:
        
        # buscar entidad en repositorio 
        saved_dishes:list[Dish] | Exception = await self.__repository.searchAllDishes()
        #VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_dishes,Exception):
            return Error_Response(saved_dishes)
        #-----
        
        #CREAR RESPONSE
        dishes_response:list[SearchById_Dish_Response] = []
        for dish in saved_dishes:
            response = SearchById_Dish_Response(
                    dish.id.id,
                    dish.name.name,
                    dish.description.description,
                    dish.price.price,
                    None
            )
            if dish.recipe is not None:
                ingredient_list:list[tuple[str, int]] = []
                for i in dish.recipe.ingredients:
                    ingredient:Ingredient | Exception = await self.__foodrepository.searchIngredientbyId(i[0])
                    if not isinstance(ingredient,Exception):
                        ingredient_list.append((ingredient.name_Ingredient.name, i[1]))
                response.recipe = (ingredient_list, dish.recipe.instructions)

            dishes_response.append(response)
        return SearchAll_Dish_Response(dishes_response)