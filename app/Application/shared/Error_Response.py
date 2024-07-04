from app.Application.shared.IService import IService_Response, Result_Type


class Error_Response(IService_Response):
    def __init__(self, error:any) -> None:
        super().__init__(type=Result_Type.Error)
        self.description = error
    

class NotFound_Response(IService_Response):
    def __init__(self) -> None:
        super().__init__(type=Result_Type.Result)
        self.description = "Id don't exists in database"