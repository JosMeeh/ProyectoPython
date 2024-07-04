from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Ingredient.Ingredient_Factory import Ingredient_Factory
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient

# Servicio para consultar un ingrediente por id

# Define los parametros que va a recibir el servicio
class SearchById_Ingredient_Parameter(IService_Parameter):
    def __init__(self, id: str) -> None:
        super().__init__(Service_Type.Query_by_Id)
        self.id = id

# Define la respuesta del servicio
class SearchById_Ingredient_Response(IService_Response):
    def __init__(self, id: str, name: str, amount: int) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.amount = amount


""" 
Servicio para consultar un ingrediente por su id

"""


class SearchById_Ingredient_Service(IService):
    def __init__(self, repository: Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Ingredient_Factory()

    async def execute(self, servicePO: SearchById_Ingredient_Parameter) -> IService_Response:
        # crear con fabrica el Id
        id_ingredient: Id_Ingredient = self.__factory.createId(servicePO.id)

        # buscar entidad en repositorio
        saved_ingredient: Ingredient | None | Exception = await self.__repository.searchIngredientbyId(id_ingredient)

        # VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_ingredient, Exception):
            return Error_Response(saved_ingredient)
        if saved_ingredient is None:
            return NotFound_Response()
        # -----

        # CREAR RESPONSE
        response = SearchById_Ingredient_Response(
            servicePO.id,
            saved_ingredient.name_Ingredient.name,
            saved_ingredient.amount_Ingredient.amount
        )

        return response