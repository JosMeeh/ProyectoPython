from abc import ABC, abstractmethod
from enum import Enum

"""
    Tipos de servicios
"""
class Service_Type(Enum):
    Command_Create = "Command_Create"
    Command_Update = "Command_Update"
    Command_Delete = "Command_Delete"
    Query_by_Id    = "Query_Id"
    Query_all      = "Query_all" 


"""
    Tipos de respuestas
"""
class Result_Type(Enum):
    Result = "Result"
    Error = "Error"

""" 
    Parameter Object genérico para la interfaz de servicio.
    Cada servicio tiene su propio IService_Parameter y deben compartir el mismo Service_Type
"""
class IService_Parameter:
    def __init__(self, type:Service_Type) -> None:
        super().__init__()
        self.__type = type

    @property
    def type(self) -> Service_Type:
        return self.__type 
    
""" 
    Response Object genérico para la interfaz de servicio.
    Identifica el tipo de dato de retorno. Permite el manejo de excepciones como respuesta válida
"""
class IService_Response:
    def __init__(self, type:Result_Type) -> None:
        super().__init__()
        self.__type = type

    @property
    def type(self) -> Result_Type:
        return self.__type 

"""
    Interfaz de servicio en la capa de aplicación
"""
class IService(ABC):
    @abstractmethod
    async def execute(self, servicePO:IService_Parameter) -> IService_Response:
        pass