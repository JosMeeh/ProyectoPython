from pydantic import UUID4, BaseModel


class DishDTO(BaseModel):
    name:str
    description:str
    price:float
    ingredient_id_list:list[tuple[UUID4, int]]
    instructions:str


class DishUpdateDTO(BaseModel):
    id:UUID4
    name:str
    description:str
    price:float
    ingredient_id_list:list[tuple[UUID4, int]]
    instructions:str


