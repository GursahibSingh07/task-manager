# calc.py v2

import click
import storage
import commands

tasks = {}

@click.group()
def cli():
    """Task manager"""
    pass

@cli.command()
def list():
   commands.list()

@cli.command()
@click.argument("task_name", type = click.STRING) 
@click.option("--description", "-desc", type = click.STRING, help = "Sentence describing task", default = "Complete by deadline")
def add_task(task_name,description):
    commands.add_input(description, task_name)
    
if __name__ == "__main__":
    cli()