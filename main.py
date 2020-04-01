clientes='pablo, ricardo, '
def create_client(client_name):
    global clientes
    clientes+=client_name
    _add_coma()


def _add_coma():
    global clientes
    clientes+=','


def list_client():
    global clientes
    print(clientes)


if __name__=='__main__':
    list_client()
    create_client('David')
    list_client()