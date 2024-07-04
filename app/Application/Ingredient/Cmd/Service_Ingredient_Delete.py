from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Ingredient.Ingredient_Factory import Ingredient_Factory
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository

# Servicio para eliminar un ingrediente

# Define los parametros que va a recibir el servicio
class Delete_Ingredient_Parameter(IService_Parameter):
    def __init__(self, id: str) -> None:
        super().__init__(Service_Type.Command_Delete)
        self.id = id

# Define la respuesta que va a devilver el servicio
class Delete_Ingredient_Response(IService_Response):
    def __init__(self, id: str, name: str, amount: int) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.amount = amount

#Servicio para la eliminacion de un ingrediente
class Delete_Ingredient_Service(IService):
    def __init__(self, repository: Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Ingredient_Factory()

    async def execute(self, servicePO: Delete_Ingredient_Parameter) -> IService_Response:
        id_ingredient: Id_Ingredient = self.__factory.createId(servicePO.id)
        search_ingredient: Ingredient | None | Exception = await self.__repository.searchIngredientbyId(id_ingredient)

        # VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(search_ingredient, Exception):
            return Error_Response(search_ingredient)
        if search_ingredient is None:
            return NotFound_Response()
        # -----

        # CREAR RESPONSE
        response = Delete_Ingredient_Response(
            servicePO.id,
            search_ingredient.name_Ingredient.name,
            search_ingredient.amount_Ingredient.amount,
        )

        deleted_ingredient: Ingredient | Exception = await self.__repository.deleteIngredient(id_ingredient)
        # VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(deleted_ingredient, Exception):
            return Error_Response(deleted_ingredient)
        # -----
        return response