from fastapi import FastAPI, HTTPException
import uvicorn

from models import ListItem

app = FastAPI()

todo_list = []
priority_name_map = {}

@app.get('/')
def hello_world():
    return 'Hello World!'


@app.get('/missing-list/', status_code=200)
def get_missing_priorities():
    global priority_name_map

    missing_priorities = []
    prioties_list = list(priority_name_map.keys())
    prioties_list.sort()

    for i in range(0, len(prioties_list)-1):
        if prioties_list[i]+1 != prioties_list[i+1]:
            missing_range = range(prioties_list[i]+1, prioties_list[i+1])
            missing_priorities += (list(missing_range))

    return missing_priorities


@app.get('/list/', status_code=200)
def get_list():
    global priority_name_map
    return priority_name_map


@app.post('/list/', status_code=201)
def add_to_list(list_item: ListItem):
    name = list_item.itemName
    priority = list_item.priority

    global todo_list
    global priority_name_map

    if priority in priority_name_map:
        # already exists
        raise HTTPException(status_code=422, detail="Item already exists")

    todo_list.append(priority)

    priority_name_map[priority] = name

    return priority_name_map


@app.delete('/list/{priority}', status_code=200)
def remove_from_list(priority: int):
    global todo_list
    global priority_name_map

    if priority not in priority_name_map:
        # doesn't exist
        raise HTTPException(status_code=404, detail="Item not found")

    todo_list.remove(priority)
    priority_name_map.pop(priority)

    return priority_name_map


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
