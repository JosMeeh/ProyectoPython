from app.Application.Ingredient.Query.Service_Ingredient_ById import SearchById_Ingredient_Response
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Ingredient.Ingredient_Factory import Ingredient_Factory
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient import Ingredient


class SearchAll_Ingredient_Parameter(IService_Parameter):
    def __init__(self) -> None:
        super().__init__(Service_Type.Query_all)
        self.id = id


class SearchAll_Ingredient_Response(IService_Response):
    def __init__(self, ingredients: list[SearchById_Ingredient_Response]) -> None:
        super().__init__(Result_Type.Result)
        self.ingredients = ingredients


""" 

"""

class SearchAll_Ingredient_Service(IService):
    def __init__(self, repository: Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Ingredient_Factory()

    async def execute(self, servicePO: SearchAll_Ingredient_Parameter) -> IService_Response:

        # buscar entidad en repositorio
        saved_ingredients: list[Ingredient] | Exception = await self.__repository.searchAllIngredients()

        # VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_ingredients, Exception):
            return Error_Response(saved_ingredients)
        # -----

        # CREAR RESPONSE
        ingredients_response: list[SearchById_Ingredient_Response] = []
        for ingredient in saved_ingredients:
            response = SearchById_Ingredient_Response(
                ingredient.getId().id,
                ingredient.name_Ingredient.name,
                ingredient.amount_Ingredient.amount
            )

            ingredients_response.append(response)

        return ingredients_response