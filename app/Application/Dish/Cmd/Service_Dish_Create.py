from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Repository import Dish_Repository


from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Description_Dish, Id_Dish, Name_Dish, Price_Dish, Recipe
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient


class Create_Dish_Parameter(IService_Parameter):
    def __init__(self, name:str, description:str, price:float, recipe:tuple[list[tuple[int, int]],str]) -> None:
        super().__init__(Service_Type.Command_Create)
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe


class Create_Dish_Response(IService_Response):
    def __init__(self, name:str, description:str, price:float, recipe:tuple[list[tuple[str, int]],str]) -> None:
        super().__init__(Result_Type.Result)
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe


""" 

"""
class Create_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__factory = Dish_Factory()

    async def execute(self, servicePO: Create_Dish_Parameter) -> IService_Response:
        # crear con fabrica el Agregado Dish
        
        new_dish:Dish = self.__factory.create(
            "--",
            servicePO.name,
            servicePO.description,
            servicePO.price,
            servicePO.recipe
        )
        # guardar entidad en repositorio 
        saved_dish:Dish | Exception = await self.__repository.addDish(new_dish)
        #VALIDAR QUE SE HA GUARDADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_dish,Exception):
            return Error_Response(saved_dish)
        #-----

        #CREAR RESPONSE
        response = Create_Dish_Response(
            servicePO.name,
            servicePO.description,
            servicePO.price,
            servicePO.recipe

        )

        return response