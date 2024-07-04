from __future__ import annotations
from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Result_Type, Service_Type
from app.Application.shared.Error_Response import Error_Response, NotFound_Response
from app.Domain.Dish.Dish_Factory import Dish_Factory
from app.Domain.Order.Order import Order
from app.Domain.Order.Order_Factory import Order_Factory
from app.Domain.Order.Order_Repository import Order_Repository
from app.Domain.Dish.Dish_Repository import Dish_Repository
from app.Domain.Dish.Dish import Dish
from app.Domain.Order.OrderVO import Order_ID
from app.Domain.Dish.Dish_VO import Id_Dish
from app.Domain.Ingredient.Ingredient import Ingredient
from app.Domain.Ingredient.Ingredient_Repository import Ingredient_Repository
from app.Domain.Ingredient.Ingredient_VO import Id_Ingredient

# Servicio para consultar una orden por id

# Define los parametros que va a recibir el servicio
class SearchById_Order_Parameter(IService_Parameter):
    def __init__(self, id: str) -> None:
        super().__init__(Service_Type.Query_by_Id)
        self.id = id

# Define la respuesta del servicio
class SearchById_Order_Response(IService_Response):
    def __init__(self, id: str, client_name: str,  price: float,
                 order_dish_list: list[tuple[str, int]]) -> None:
        super().__init__(Result_Type.Result)
        self.id = id
        self.client_name = client_name
        self.price = price
        self.order_dish_list = order_dish_list


""" 

"""


class SearchById_Order_Service(IService):
    def __init__(self, repository: Order_Repository, dish_repository: Dish_Repository) -> None:
        super().__init__()
        self.__repository = repository
        self.__foodrepository = dish_repository
        self.__factory = Order_Factory()

    async def execute(self, servicePO: SearchById_Order_Parameter) -> IService_Response:
        # crear con fabrica el Id
        id_order: Order_ID = servicePO.id
        # buscar entidad en repositorio
        saved_order: Order | None | Exception = await self.__repository.searchOrderbyId(id_order)
        return saved_order
        # VALIDAR QUE SE HA BUSCADO EL AGREGADO CORRECTAMENTE:
        if isinstance(saved_order, Exception):
            return Error_Response(saved_order)
        if saved_order is None:
            return NotFound_Response()
        # -----

        # CREAR RESPONSE
        response = SearchById_Order_Response(
            servicePO.id,
            saved_order.cliente_name,
            saved_order.amount,
            None
        )
        if saved_dish.recipe is not None:
            ingredient_list: list[tuple[str, int]] = []
            for i in saved_dish.recipe.ingredients:
                ingredient: Ingredient | Exception = await self.__dish_repository.searchIngredientbyId(i[0])
                if not isinstance(ingredient, Exception):
                    ingredient_list.append((ingredient.name_Ingredient.name, i[1]))
            response.recipe = (ingredient_list, saved_dish.recipe.instructions)

        return response