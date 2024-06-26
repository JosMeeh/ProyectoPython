from abc import ABC, abstractmethod
from enum import Enum

class Service_Type(Enum):
    Command_Create = "Command_Create"
    Command_Update = "Command_Update"
    Command_Delete = "Command_Delete"
    Query_by_Id    = "Query_Id"
    Query_all      = "Query_all" 

class Result_Type(Enum):
    Result = "Result"
    Error = "Error"

""" 

"""
class IService_Parameter:
    def __init__(self, type:Service_Type) -> None:
        super().__init__()
        self.__type = type

    @property
    def type(self) -> Service_Type:
        return self.__type 
    
""" 

"""
class IService_Response:
    def __init__(self, type:Result_Type) -> None:
        super().__init__()
        self.__type = type

    @property
    def type(self) -> Result_Type:
        return self.__type 




"""

"""
class IService(ABC):
    @abstractmethod
    async def execute(self, servicePO:IService_Parameter) -> IService_Response:
        pass