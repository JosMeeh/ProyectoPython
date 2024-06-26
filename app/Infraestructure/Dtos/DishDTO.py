from pydantic import BaseModel

class DishDTO(BaseModel):
    name:str
    description:str
    price:float
    ingridient_id_list:list[tuple[int, int]]
    instructions:str

