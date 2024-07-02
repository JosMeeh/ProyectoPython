from pydantic import UUID4, BaseModel

class DishDTO(BaseModel):
    name:str
    description:str
    price:float
    ingridient_id_list:list[tuple[str, int]]
    instructions:str

class DishUpdateDTO(BaseModel):
    id:UUID4
    name:str
    description:str
    price:float
    ingridient_id_list:list[tuple[str, int]]
    instructions:str


