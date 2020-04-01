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


def Print_Welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__=='__main__':
    Print_Welcome()
    
    command=input('::')

    if command.upper()=='C':
        client_name=input('What is the client name? ')
        create_client(client_name)
        list_client()
    elif command.upper()=='D':
            pass
    else:
        print('Invalid command')