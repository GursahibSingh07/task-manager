import json
import os

Task_file = "tasks.json"
tasks = {}

def load_tasks():
    global tasks
    if not os.path.exists(Task_file):
        with open(Task_file, mode = "w") as file:
            json.dump([], file)

    with open(Task_file, mode = "r") as file:
        tasks =  json.load(file)

load_tasks()

def export_tasks():
    return tasks

def import_tasks(modified_tasks):
    global tasks
    tasks = modified_tasks
    with open(Task_file, mode = "w") as file:
        json.dump(tasks, file)

