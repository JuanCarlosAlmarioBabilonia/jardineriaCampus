import storage.cliente as cli
from tabulate import tabulate
def getAllClientesName():
    clienteName = list()
    for val in cli.cliente:
        codigoName = dict({
        "Codigo": val.get("codigo_cliente"),
        "Nombre del Cliente": val.get("nombre_cliente")
        })
        clienteName.append(codigoName)
    return clienteName
def getOneClientCodigo(codigo):
    for val in cli.cliente:
        if(val.get("codigo_cliente") == codigo):
            return[{
        "Codigo del Cliente": val.get("codigo_cliente"),
        "Nombre del Cliente": val.get("nombre_cliente")   
            }]
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.cliente:
        if(val.get("limite_credito") >= limiteCredit and val.get("ciudad") == ciudad):
            clienteCredic.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre del Ciente":val.get("nombre_cliente"),
                "Director":f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direcciones":f"{val.get('ciudad')} {val.get('region')} {val.get('pais')} {val.get('codigo_postal')}",
                "Origen":val.get("codigo_cliente"),
                "Codigo del Asesor":val.get("codigo_empleado_rep_ventas"),
                "Credito":val.get("limite_credito")
            })

    return clienteCredic
def getAllClientPaisRegionCiudad(pais, region = None, ciudad = None):
    clientZone = list()
    for val in cli.cliente:
        if(
            val.get("pais")== pais or 
            (val.get("region") == region or val.get("region") == None) or
            (val.get("ciudad") == ciudad or val.get("ciudad") == None)
        ):
            clientZone.append({
                "Codigo del cliente":val.get("codigo_cliente"),
                "Nombre del cliente":val.get("nombre_cliente"),
                "Nombre del contacto":val.get("nombre_contacto"),
                "Apellido del contacto":val.get("apellido_contacto"),
                "Ciudad":val.get("ciudad"),
                "Region":val.get("region"),
                "Pais":val.get("pais")
            })
    return clientZone
def getAllClientCodigoPostal():
    clientCodigoPostal= list()
    for val in cli.cliente:
        codigoPostal=dict({
        "Codigo del cliente": val.get("codigo_cliente"),
        "Nombre del cliente": val.get("nombre_cliente"),
        "Nombre del contacto":val.get("nombre_contacto"),
        "Apellido del contacto":val.get("apellido_contacto"),
        "Codigo postal": val.get("codigo_postal")
        })
        clientCodigoPostal.append(codigoPostal)
    return(clientCodigoPostal)
def getAllClientCiudad(ciudad):
    clientCity = list()
    for val in cli.cliente:
        if(
        (val.get("ciudad") == ciudad)
        ):
            clientCity.append({
                "Codigo del cliente":val.get("codigo_cliente"),
                "Nombre del cliente":val.get("nombre_cliente"),
                "Nombre del contacto":val.get("nombre_contacto"),
                "Apellido del contacto":val.get("apellido_contacto"),
                "Ciudad":val.get("ciudad")
            })
    return clientCity
def getAllClientDireccion():
    clientDireccion=list()
    for val in cli.cliente:
        direccion=dict({
        "Codigo del cliente": val.get("codigo_cliente"),
        "Nombre del cliente": val.get("nombre_cliente"),
        "Nombre del contacto":val.get("nombre_contacto"),
        "Apellido del contacto":val.get("apellido_contacto"),
        "Direccion principal": val.get("linea_direccion1")
        })
        clientDireccion.append(direccion)
    return(clientDireccion)
def getAllClientCreditEntre():
    clientCredit=list()
    for val in cli.cliente:
        if(val.get("limite_credito")>=5000 and val.get("limite_credito")<=10000):
            clientCredit.append({
                "Codigo del cliente":val.get("codigo_cliente"),
                "Nombre del cliente":val.get("nombre_cliente"),
                "Nombre del contacto":val.get("nombre_contacto"),
                "Apellido del contacto":val.get("apellido_contacto"),
                "Limite del credito":val.get("limite_credito")
            })
    return clientCredit
def getAllClientTelefono():
    clientTelefono= list()
    for val in cli.cliente:
        telefono=dict({
        "Codigo del cliente":val.get("codigo_cliente"),
        "Nombre del cliente":val.get("nombre_cliente"),
        "Nombre del contacto":val.get("nombre_contacto"),
        "Apellido del contacto":val.get("apellido_contacto"),
        "Telefono": val.get("telefono")
        })
        clientTelefono.append(telefono)
    return(clientTelefono)
def getAllNombreClienteEspañol():
    clienteEspañol=[]
    for val in cli.cliente:
        if(val.get("pais")=="Spain"):
            clienteEspañol.append(
                {
                "Codigo del cliente":val.get("codigo_cliente"),
                "Nombre del cliente":val.get("nombre_cliente"),
                "Nombre del contacto":val.get("nombre_contacto"),
                "Apellido del contacto":val.get("apellido_contacto"),
                "Pais":val.get("pais")  
                }
            )
    return clienteEspañol
def menu():
    print("""
REPORTES DE LOS CLIENTES
1. Obtener todos los clientes (codigo y nombre)
2. Obtener un cliente por el codigo
3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad a la que pertenece (ejem: 3000.0 - San Francisco)
4. Obtener todos los clientes del pais, region y ciudad ingresados
5. Obtener el codigo postal de todos los clientes
6. Obtener todos los clientes de la ciudad ingresada
7. Obtener la direccion de todos los clientes
8. Obtener todos los clientes que posean un credito entre 5000 y 10000
9. Obtener el telefono de todos los clientes
10. Obtener el nombre de todos los clientes españoles
""")
    op=int(input("Seleccione una de las opciones: "))
    if(op==1):
        print(tabulate(getAllClientesName(),headers="keys",tablefmt="grid"))
    elif(op==2):
        codigoCliente=int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getOneClientCodigo(codigoCliente),headers="keys",tablefmt="grid"))
    elif(op==3):
        limite=float(input("Ingrese el limite de credito de los clientes que desea visualizar: "))
        ciudad=input("Ingrese el nombre de la ciudad de la que desea filtrar los clientes: ")
        print(tabulate(getAllClientCreditoCiudad(limite,ciudad),headers="keys",tablefmt="grid"))
    elif(op==4):
        pais=input("Ingrese el pais del cliente con mayuscula(s) inicial(es): ")
        region=input("Ingrese la region del cliente con mayuscula(s) inicial(es): ")
        ciudad=input("Ingrese la ciudad del cliente con mayuscula(s) inicial(es): ")
        print(tabulate(getAllClientPaisRegionCiudad(pais,region,ciudad),headers="keys",tablefmt="grid"))
    elif(op==5):
        print(tabulate(getAllClientCodigoPostal(),headers="keys",tablefmt="grid"))
    elif(op==6):
        ciudad=input("Ingrese la ciudad con mayuscula(s) inicial(es): ")
        print(tabulate(getAllClientCiudad(ciudad),headers="keys",tablefmt="grid"))
    elif(op==7):
        print(tabulate(getAllClientDireccion(),headers="keys",tablefmt="grid"))
    elif(op==8):
        print(tabulate(getAllClientCreditEntre(),headers="keys",tablefmt="grid"))
    elif(op==9):
        print(tabulate(getAllClientCreditEntre(),headers="keys",tablefmt="grid"))
    elif(op==10):
         print(tabulate(getAllNombreClienteEspañol(),headers="keys",tablefmt="grid"))
