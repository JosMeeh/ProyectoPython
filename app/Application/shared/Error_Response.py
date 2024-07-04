from app.Application.shared.IService import IService_Response, Result_Type

"""
    IService_Response
    type = Error

    Respuesta para Excepciones genérica.
    Permite encapsular el error y emitirlo como una respuesta válida para el usuario
"""
class Error_Response(IService_Response):
    def __init__(self, error:any) -> None:
        super().__init__(type=Result_Type.Error)
        self.description = error
    
"""
    IService_Response
    type = Result

    Respuesta si dentro del sistema no se consiguió el item que se bsuca.
    Permite enviar un mensaje al usuario al respecto
"""
class NotFound_Response(IService_Response):
    def __init__(self) -> None:
        super().__init__(type=Result_Type.Result)
        self.description = "Id don't exists in database"