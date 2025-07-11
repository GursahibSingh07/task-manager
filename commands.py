import click
import storage

def list():
    tasks = storage.export_tasks()
    for key,value in tasks.items():
        click.echo(f"{key} : {value}")
        click.echo("----")

def add_input(task_description,task_name):
    tasks = storage.export_tasks()
    tasks[task_name] = task_description
    storage.import_tasks(tasks)
