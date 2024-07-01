from __future__ import annotations
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Ingredient.Ingredient_Factory import Ingredient_Factory
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient import Ingredient


class Create_Ingredient_Parameter(IService_Parameter):
    def __init__(self, name: str, amount: int) -> None:
        super().__init__(Service_Type.Command_Create)
        self.name = name
        self.amount = amount


class Create_Ingredient_Response(IService_Response):
    def __init__(self, name: str, amount: int) -> None:
        super().__init__(Result_Type.Result)
        self.name = name
        self.amount = amount


""" 

"""


class Create_Ingredient_Service(IService):
    def __init__(self, repository: Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Ingredient_Factory()

    async def execute(self, servicePO: Create_Ingredient_Parameter) -> IService_Response:
        # crear con fabrica el Agregado Ingredient

        new_ingredient: Ingredient = self.__factory.create(
            "--",
            servicePO.name,
            servicePO.amount,
        )

        # guardar entidad en repositorio
        saved_ingredient: Ingredient | Exception = await self.__repository.addIngredient(new_ingredient)
        # VALIDAR QUE SE HA GUARDADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_ingredient, Exception):
            return Error_Response(saved_ingredient)
        # -----

        # CREAR RESPONSE
        response = Create_Ingredient_Response(
            servicePO.name,
            servicePO.amount
        )
        return response
