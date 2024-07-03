from pydantic import UUID4, BaseModel

class MenuDTO(BaseModel):
    name:str
    dish_list:set[UUID4]

class MenuUpdateDTO(BaseModel):
    id:UUID4
    name:str
    dish_list:set[UUID4]