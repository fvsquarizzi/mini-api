from pydantic import BaseModel, Field
from itertools import count 

id_counter = count(1)
    
class TaskRequestSchema(BaseModel):
    title: str = Field(min_length=3) 
    done: bool

class TaskResponseSchema(TaskRequestSchema):
    id: int = Field(default_factory=lambda: next(id_counter))
    
class TaskListResponseSchema(BaseModel):
    tasks: list[TaskResponseSchema]
    total: int