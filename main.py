import sys

#variables globales
clientes=['pablo', 'ricardo']

#Funciones de reutilizacion de codigo
def get_client_name():
    client_name=None
    while not client_name:
        client_name=input('What is the client name?: ')

        if client_name=='exit':
            client_name=None
            break
        
    if not client_name:
        sys.exit()
            
    return client_name


def get_not_in_list():
    return print('Client not in client\'s list')


#Funciones de iteraccion directa CRUD
def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes.append(client_name)
    else:
        print('Clien alredy is in the client\'s list')


def list_client():
    for idx, client in enumerate(clientes):
        print('{}:{}'.format(idx, client))


def update_Client(client_name, updated_client_name):
    global clientes
    if client_name in clientes:
        index=clientes.index(client_name)
        clientes[index]=updated_client_name
    else:
        get_not_in_list()


def delete_client(client_name):
    global clientes
    if client_name in clientes:
        clientes.remove(client_name)
    else:
        get_not_in_list()


def search_client(client_name):
    for client in clientes:
        if client != client_name:
            continue
        else:
            return True

#Funcione de menu
def Print_Welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

#Procesos de inicio main de aqui se va ejecutando en orden y se
# llama a las fucniones segun se requieran 
if __name__=='__main__':
    Print_Welcome()
    command=input('::')
    command=command.upper()

    #seleccion e invocacion de funciones segun lo 
    # que seleccione el usuario
    if command=='C':
        client_name=get_client_name()
        create_client(client_name)
        list_client()
    elif command=='L':
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
    elif command=='S':
        client_name=get_client_name()
        found=search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))        
    else:
        print('Invalid command')