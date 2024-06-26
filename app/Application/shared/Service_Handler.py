from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Service_Type

""" 

"""
class IService_Response:
    def __init__(self) -> None:
        self.__services:dict[Service_Type, IService] = []

    def execute(self, servicePO:IService_Parameter) -> IService_Response:
        #PROBAR LO QUE SUCEDE SI NO EXISTE TAL TIPO DE SERVICIO
        response = self.__services[servicePO.type].execute(servicePO)
        return response

    def addService(self, type:Service_Type, service:IService) -> None:
        self.__services.update({type:service})