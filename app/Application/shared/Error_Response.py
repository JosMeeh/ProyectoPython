from app.Application.shared.IService import IService_Response, Result_Type


class Error_Response(IService_Response):
    def __init__(self, error) -> None:
        super().__init__(type=Result_Type.Error)
        self.description = error

    @property
    def type(self) -> Result_Type:
        return self.__type 