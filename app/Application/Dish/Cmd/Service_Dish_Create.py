from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response
from app.Domain.Dish.Dish import Dish
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository

"""
    IService_Parameter
    type = Command_Create

    Parameter Object para Servicio de Create de Platillo.
    Recibe todos los valores primitivos de un platillo excepto su id que es generada en el servicio
"""
class Create_Dish_Parameter(IService_Parameter):
    def __init__(self, name:str, description:str, price:float, recipe:tuple[list[tuple[int, int]],str]) -> None:
        super().__init__(Service_Type.Command_Create)
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe

"""
    IService_Response
    type = Result

    Respuesta para resultado exitoso de crear un Platillo
    Emite todos los valores primitivos de un platillo excepto su id
"""
class Create_Dish_Response(IService_Response):
    def __init__(self, name:str, description:str, price:float, recipe:tuple[list[tuple[str, int]],str]) -> None:
        super().__init__(Result_Type.Result)
        self.name = name
        self.description = description
        self.price = price
        self.recipe = recipe


""" 
    IService
    type = Command_Create

    Servicio para crear un Platillo
"""
class Create_Dish_Service(IService):
    def __init__(self, repository:Dish_Repository, food_repository:Ingredient_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = food_repository 
        self.__factory = Dish_Factory()

    async def execute(self, servicePO: Create_Dish_Parameter) -> IService_Response:
        """ 
            Crear un platillo en base de datos con los datos pasados por parametro
            En caso de alguna excepcion en base de datos retorna un "Error_Response"
        """
        #crear con fabrica el Agregado Dish
        new_dish:Dish = self.__factory.create(
            "--",
            servicePO.name,
            servicePO.description,
            servicePO.price,
            servicePO.recipe
        )

        #Guardar agregado en repositorio 
        saved_dish:Dish | Exception = await self.__repository.addDish(new_dish)
        #Validar Respuesta
        if isinstance(saved_dish,Exception):
            return Error_Response(saved_dish)
        #-----
    
        #CREAR RESPONSE
        response = Create_Dish_Response(
            servicePO.name,
            servicePO.description,
            servicePO.price,
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