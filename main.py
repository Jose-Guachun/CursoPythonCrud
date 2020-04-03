clientes='pablo, ricardo, '
def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes+=client_name
        _add_coma()
    else:
        print('Clien alredy is in the client\'s list')


def _add_coma():
    global clientes
    clientes+=','


def list_client():
    global clientes
    print(clientes)


def update_Client(client_name, updated_client_name):
    global clientes
    if client_name in clientes:
        clientes=clientes.replace(client_name+',',updated_client_name+',')
    else:
        print('Client is not in client list')


def delete_client(client_name):
    global clientes
    if client_name in clientes:
        clientes=clientes.replace(client_name+',', '')
    else:
        pass
def Print_Welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')


def get_client_name():
    return input('What is the client name?: ')


if __name__=='__main__':
    Print_Welcome()
    
    command=input('::')
    command=command.upper()

    if command=='C':
        client_name=get_client_name()
        create_client(client_name)
        list_client()
    elif command=='D':
            client_name=get_client_name()
            delete_client(client_name)
            list_client()
    elif command=='U':
            client_name=get_client_name()
            update_Client_name=input('What is the update name client?: ')
            update_Client(client_name, update_Client_name)
            list_client()
    else:
        print('Invalid command')