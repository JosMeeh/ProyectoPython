from app.Application.shared.IService import IService, IService_Parameter, IService_Response, Service_Type

"""
    Clase que permite el control y asignación de el servicio según los parámetros y endpoint
    que se quieren utilizar.
"""
class Service_Handler:
    def __init__(self) -> None:
        # Crear un diccionario para guardar los servicios
        self.__services:dict[Service_Type, IService] = {}

    async def execute(self, servicePO:IService_Parameter) -> IService_Response:
        """ 
            Ejecuta el servicio que coincida con el tipo del parámetro IService_Parameter
        """
        response = await self.__services[servicePO.type].execute(servicePO)
        return response


    def addService(self, type:Service_Type, service:IService) -> None:
        """ 
            Añade un nuevo servicio al diccionario del Service_Handler
        """
        self.__services.update({type:service})
