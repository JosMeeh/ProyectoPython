from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Ingredient.Ingredient_Factory import Ingredient_Factory
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository


class Update_Ingredient_Parameter(IService_Parameter):
    def __init__(self, id: str, name: str, amount: int) -> None:
        super().__init__(Service_Type.Command_Update)

        self.id = id
        self.name = name
        self.amount = amount




class Update_Ingredient_Response(IService_Response):
    def __init__(self, id: str, name: str, amount: int) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.amount = amount

""" 

"""


class Update_Ingredient_Service(IService):
    def __init__(self, repository: Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Ingredient_Factory()

    async def execute(self, servicePO: Update_Ingredient_Parameter) -> IService_Response:

        new_ingredient = self.__factory.create(
            servicePO.id,
            servicePO.name,
            servicePO.amount
        )

        updated_ingredient: Ingredient | None | Exception = await self.__repository.updateIngredient(
            new_ingredient.getId(),
            new_ingredient.name_Ingredient,
            new_ingredient.amount_Ingredient
        )
        if isinstance(updated_ingredient, Exception):
            return Error_Response(updated_ingredient)
        if updated_ingredient is None:
            return NotFound_Response()

        # CREAR RESPONSE
        response = Update_Ingredient_Parameter(
            updated_ingredient.getId().id,
            updated_ingredient.name_Ingredient.name,
            updated_ingredient.amount_Ingredient.amount
        )

        return response