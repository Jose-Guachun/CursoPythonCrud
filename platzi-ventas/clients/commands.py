import click

from clients.services import ClientServices
from clients.models import Client

@click.group()
def clients():
    """manages the clients lifecycle"""
    pass

@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help='the client name')
@click.option('-c', '--company',
                type=str,
                prompt=True,
                help='the client company')
@click.option('-e', '--email',
                type=str,
                prompt=True,
                help='the client email')
@click.option('-p', '--position',
                type=str,
                prompt=True,
                help='the client position')                    
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a ner client"""   
    client=Client(name, company, email, position)
    client_service=ClientServices(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all client"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""   
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client"""
    pass

all=clients 
