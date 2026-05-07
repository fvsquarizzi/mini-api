from fastapi import FastAPI, HTTPException
from model import TaskRequestSchema, TaskResponseSchema, TaskListResponseSchema

app = FastAPI()

tasks: list[TaskResponseSchema] = []

@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Api is up"}

@app.post("/tasks", status_code=201)
def create_task(task: TaskRequestSchema) -> TaskResponseSchema:
    response = TaskResponseSchema(**task.model_dump())
    tasks.append(response)
    
    return response

@app.get("/tasks")
def list_tasks() -> TaskListResponseSchema:
    return TaskListResponseSchema(tasks=tasks, total=len(tasks))
    
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> TaskResponseSchema:
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="There is no task with this id")
    tasks.remove(task)
    return task