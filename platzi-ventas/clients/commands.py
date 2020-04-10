import click
@click.group()
def clients():
    """manages the clients lifecycle"""
    pass

@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a ner client"""   
    pass


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
