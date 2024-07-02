from pydantic import BaseModel

class OrderDTO(BaseModel):
    client_name:str
    order_dishes_list:list[tuple[str,int]]
    mount:float