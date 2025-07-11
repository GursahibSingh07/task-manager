# calc.py v2

import click
import storage
import commands
import datetime

tasks = {}

@click.group()
def cli():
    """Task manager"""
    pass

@cli.command()
def list():
   commands.list_task()

@cli.command()
@click.argument("task_name", type = click.STRING)
@click.option("--description", "-desc", type = click.STRING, help = "Sentence describing task anew", default = "Complete by deadline")
@click.option("--deadline", "-dead", type = click.STRING, help = "Sentence describing task's deadline anew", default = "00:00")
def add(task_name,description,deadline):
    try:
        datetime.datetime.strptime(deadline, "%H:%M")
    except ValueError:
        click.echo("Not valid Time format. Use HH:MM (e.g., 14:30)")
        return
    commands.add_task(task_name, description, deadline)

@cli.command()
@click.argument("task_name", type = click.STRING) 
def remove(task_name):
    commands.remove_task(task_name)

@cli.command()
@click.argument("task_name", type = click.STRING)
@click.option("--newname", "-nn", type = click.STRING, help = "New task name", default =None)
@click.option("--description", "-desc", type = click.STRING, help = "Sentence describing task", default = None)
@click.option("--deadline", "-dead", type = click.STRING, help = "Sentence describing task's deadline", default = None)
def edit(task_name,newname, description, deadline):
    try:
        datetime.datetime.strptime(deadline, "%H:%M")
    except ValueError:
        click.echo("Not valid Time format. Use HH:MM (e.g., 14:30)")
        return
    commands.edit_task(task_name,newname,description, deadline)
    
if __name__ == "__main__":
    cli()