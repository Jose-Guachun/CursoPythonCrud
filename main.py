import sys 
import csv
import os
#variables globales
CLIENT_TABLE='./clients.csv'
CLIENT_SCHEMA=['name', 'company', 'email', 'position']
clientes=[]


#fUNCIONES DE MANEJO DE ARCHIVO
def _ini_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader=csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clientes.append(row)

def _save_clients_to_storage():
    tmp_table_name='{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name ,mode='w') as f:
        writer= csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clientes)
        
        os.remove(CLIENT_TABLE)
        f.close()
        os.rename(tmp_table_name, CLIENT_TABLE)

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


def get_client_field(field_name):
    field=None
    while not field:
        field=input('What is the client {}?'.format(field_name))
    return field

def get_client_from_user():
    client = {
        'name': get_client_field('name'),
        'company': get_client_field('company'),
        'email': get_client_field('email'),
        'position': get_client_field('position'),
    }

    return client
#Funciones de iteraccion directa CRUD
def create_client(client):
    global clientes
    if client not in clientes:
        clientes.append(client)
    else:
        print('Clien alredy is in the client\'s list')


def list_client():
    global clientes
    for idx, client in enumerate(clientes):
        print('{uid}|{name}|{company}|{email}|{position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))



def update_client(client_id, updated_client):
    global clientes

    if len(clientes) - 1 >= client_id:
        clientes[client_id] = updated_client
    else:
        get_not_in_list


def delete_client(client_id):
    global clientes
    for idx in enumerate(clientes):
        if idx==client_id:
            del clientes[idx]
            break


def search_client(client_name):
    for client in clientes:
        if client['name'] != client_name:
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
    _ini_clients_from_storage()
    Print_Welcome()
    command=input('::')
    command=command.upper()

    #seleccion e invocacion de funciones segun lo 
    # que seleccione el usuario
    if command=='C':
        client=get_client_from_user()
        create_client(client)
        
    elif command=='L':
        list_client()
    elif command=='D':
        client_id=int(get_client_field('id'))
        delete_client(client_id)
        
    elif command=='U':
        client_id=int(get_client_field('id'))
        updated_client=get_client_from_user()
        update_client(client_id, updated_client)
        
    elif command=='S':
        client_name=get_client_field('name')
        found=search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))        
    else:
        print('Invalid command')

    _save_clients_to_storage()