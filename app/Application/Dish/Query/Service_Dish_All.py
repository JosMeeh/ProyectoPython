from __future__ import annotations

from app.Application.Dish.Query.Service_Dish_ById import SearchById_Dish_Response
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Dish.Dish import Dish
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository

"""
    IService_Parameter
    type = Query_all

    Parameter Object para Servicio de mostrar todos los Platillos.
"""
class SearchAll_Dish_Parameter(IService_Parameter):
    def __init__(self) -> None:
        super().__init__(Service_Type.Query_all)
        self.id = id

"""
    IService_Response
    type = Result

    Respuesta para resultado exitoso de mostrar todos los Platillos
    Emite una lista con todos los platillos y todos los valores primitivos
"""
class SearchAll_Dish_Response(IService_Response):
    def __init__(self, dishes:list[SearchById_Dish_Response]) -> None:
        super().__init__(Result_Type.Result)
        self.dishes = dishes

""" 
    IService
    type = Query_all

    Servicio para mostrar todos los Platillos
"""
class SearchAll_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository, food_repository:Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 

    async def execute(self, servicePO: SearchAll_Dish_Parameter) -> IService_Response:
        """ 
            Busca todos los platillos guardados en la base de datos y los agrupa en una lista
            En caso de alguna excepcion en base de datos retorna un "Error_Response"
        """
        # buscar entidades en repositorio 
        saved_dishes:list[Dish] | Exception = await self.__repository.searchAllDishes()
        #Validar Respuesta
        if isinstance(saved_dishes,Exception):
            return Error_Response(saved_dishes)
        #-----
        
        #CREAR RESPONSE
        dishes_response:list[SearchById_Dish_Response] = []
        for dish in saved_dishes:
            #Crear response individual
            response = SearchById_Dish_Response(
                    dish.id.id,
                    dish.name.name,
                    dish.description.description,
                    dish.price.price,
                    None
            )

            #Buscar el nombre de los Ingredientes de un platillo
            if dish.recipe is not None:
                ingredient_list:list[tuple[str, int]] = []
                for i in dish.recipe.ingredients:
                    ingredient:Ingredient | Exception = await self.__foodrepository.searchIngredientbyId(i[0])
                    if not isinstance(ingredient,Exception):
                        ingredient_list.append((ingredient.name_Ingredient.name, i[1]))
                response.recipe = (ingredient_list, dish.recipe.instructions)

            dishes_response.append(response)
        return SearchAll_Dish_Response(dishes_response)