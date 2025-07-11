import click
import storage

def list_task():
    i = 0
    click.echo("\n")
    tasks = storage.export_tasks()
    for key,value in tasks.items():
        i = i + 1
        click.echo(f" {i}. {key} : {value[0]} [ by {value[1]}]")
    click.echo("\n")

def add_task(task_name,task_description,task_deadline):
    tasks = storage.export_tasks()
    tasks[task_name] = [task_description, task_deadline]
    storage.import_tasks(tasks)
    click.echo(f"Added task : {task_name} succesfully")

def remove_task(task_name):
    tasks = storage.export_tasks()
    for key in list(tasks.keys()):
        if key.lower() == task_name.lower():
            del tasks[key]
            storage.import_tasks(tasks)
            click.echo(f"{task_name} succesfully removed")
            return 
    click.echo("Key not found")

def edit_task(task_name, new_name=None, task_description=None, task_deadline=None):
    tasks = storage.export_tasks()
    for key in list(tasks.keys()):
        if key.lower() == task_name.lower():
            value = tasks[key]
            if task_description is not None:
                value[0] = task_description
            if task_deadline is not None:
                value[1] = task_deadline
            if new_name is not None and new_name.lower() != key.lower():
                tasks[new_name] = value
                del tasks[key]
            else:
                tasks[key] = value
            storage.import_tasks(tasks)
            click.echo(f"Task '{key}' updated successfully.")
            return
    click.echo("Task not found")
