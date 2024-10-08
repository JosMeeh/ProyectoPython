from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository

"""
    IService_Parameter
    type = Query_by_Id

    Parameter Object para Servicio de mostrar un Platillo.
    Recibe solo la id de un platillo
"""
class SearchById_Dish_Parameter(IService_Parameter):
    def __init__(self, id:str) -> None:
        super().__init__(Service_Type.Query_by_Id)

        self.id = id

"""
    IService_Response
    type = Result

    Respuesta para resultado exitoso de mostrar un Platillo
    Emite todos los valores primitivos de un platillo
"""
class SearchById_Dish_Response(IService_Response):
    def __init__(self, id:str, name:str, description:str, price:float, recipe:tuple[list[tuple[str, int]],str]) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe


""" 
    IService
    type = Query_by_Id

    Servicio para mostrar un Platillo
"""
class SearchById_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository, food_repository:Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Dish_Factory()

    async def execute(self, servicePO: SearchById_Dish_Parameter) -> IService_Response:
        """ 
            Busca un platillo guardado en la base de datos 
            En caso de que no se consiga tal id retornara un "NotFound_Response"
            En caso de alguna excepcion en base de datos retorna un "Error_Response"
        """
        # crear con fabrica el Id
        id_dish:Id_Dish = self.__factory.createId(servicePO.id)
        # buscar entidad en repositorio 
        saved_dish:Dish | None | Exception = await self.__repository.searchDishbyId(id_dish)
        #Validar Respuesta
        if isinstance(saved_dish,Exception):
            return Error_Response(saved_dish)
        if saved_dish is None:
            return NotFound_Response()
        #-----

        #CREAR RESPONSE
        response = SearchById_Dish_Response(
            servicePO.id,
            saved_dish.name.name,
            saved_dish.description.description,
            saved_dish.price.price,
            None
        )

        #Buscar el nombre de los Ingredientes de un platillo
        if saved_dish.recipe is not None:
            ingredient_list:list[tuple[str, int]] = []
            for i in saved_dish.recipe.ingredients:
                ingredient:Ingredient | Exception = await self.__foodrepository.searchIngredientbyId(i[0])
                if not isinstance(ingredient,Exception):
                    ingredient_list.append((ingredient.name_Ingredient.name, i[1]))
            response.recipe = (ingredient_list, saved_dish.recipe.instructions)
        
        return response