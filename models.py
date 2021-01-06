from pydantic import BaseModel

class ListItem(BaseModel):
    itemName: str
    priority: int