from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository

"""
    IService_Parameter
    type = Command_Delete

    Parameter Object para Servicio de Delete de Platillo.
    Recibe solo la id de un platillo
"""
class Delete_Dish_Parameter(IService_Parameter):
    def __init__(self, id:str) -> None:
        super().__init__(Service_Type.Command_Delete)
        self.id = id

"""
    IService_Response
    type = Result

    Respuesta para resultado exitoso de eliminar un Platillo
    Emite todos los valores primitivos de un platillo
"""
class Delete_Dish_Response(IService_Response):
    def __init__(self, id:str, name:str, description:str, price:float, recipe:tuple[list[tuple[str, int]],str]) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe

""" 
    IService
    type = Command_Delete

    Servicio para eliminar un Platillo
"""
class Delete_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository, food_repository:Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Dish_Factory()

    async def execute(self, servicePO: Delete_Dish_Parameter) -> IService_Response:
        """ 
            Eliminar un platillo en base de datos a traves del Id proporcionado
            En caso de que no se consiga tal id retornara un "NotFound_Response"
            En caso de alguna excepcion en base de datos retorna un "Error_Response"
        """
        #Buscar Platillo a eliminar
        id_dish:Id_Dish = self.__factory.createId(servicePO.id)
        search_dish:Dish | None | Exception = await self.__repository.searchDishbyId(id_dish)
        #Validar Respuesta
        if isinstance(search_dish,Exception):
            return Error_Response(search_dish)
        if search_dish is None:
            return NotFound_Response()
        #-----        
        
        #CREAR RESPONSE
        response = Delete_Dish_Response(
            servicePO.id,
            search_dish.name.name,
            search_dish.description.description,
            search_dish.price.price,
            None
        )
        
        #Buscar el nombre de los Ingredientes de un platillo
        if search_dish.recipe is not None:
            ingredient_list:list[tuple[str, int]] = []
            for i in search_dish.recipe.ingredients:
                ingredient:Ingredient | Exception = await self.__foodrepository.searchIngredientbyId(i[0])
                if not isinstance(ingredient,Exception):
                    ingredient_list.append((ingredient.name_Ingredient.name, i[1]))
            response.recipe = (ingredient_list, search_dish.recipe.instructions)


        #Eliminar platillo de la base de datos
        deleted_dish:Dish | Exception = await self.__repository.deleteDish(id_dish)

        #Validar Respuesta
        if isinstance(deleted_dish,Exception):
            return Error_Response(deleted_dish)
        #-----    

        return response
