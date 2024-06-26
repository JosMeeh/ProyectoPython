from app.Application.shared.IService import IService, IService_Parameter, IService_Response

"""

"""
class IDecorator_Service(IService):
    def __init__(self, wrapee:IService) -> None:
        super().__init__()
        self._wrapee = wrapee

    async def execute(self, servicePO:IService_Parameter) -> IService_Response:
        return super().execute(servicePO)