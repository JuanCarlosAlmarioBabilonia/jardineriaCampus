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
            val.get("pais")== pais and 
            (val.get("region") == region or val.get("region") == None) or
            (val.get("ciudad") == ciudad or val.get("ciudad") == None)
        ):
            clientZone.append(val)
    return clientZone
def getAllClientCodigoPostal():
    clientCodigoPostal= list()
    for val in cli.cliente:
        codigoPostal=dict({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get("nombre_cliente"),
        "codigo_postal": val.get("codigo_postal")
        })
        clientCodigoPostal.append(codigoPostal)
    return(clientCodigoPostal)
def getAllClientCiudad(ciudad):
    clientCity = list()
    for val in cli.cliente:
        if(
        (val.get("ciudad") == ciudad)
        ):
            clientCity.append(val)
    return clientCity
def getAllClientDireccion():
    clientDireccion=list()
    for val in cli.cliente:
        direccion=dict({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get("nombre_cliente"),
        "linea_direccion1": val.get("linea_direccion1")
        })
        clientDireccion.append(direccion)
    return(clientDireccion)
def getAllClientCreditEntre():
    clientCredit=list()
    for val in cli.cliente:
        if(val.get("limite_credito")>=5000 and val.get("limite_credito")<=10000):
            clientCredit.append(val)
    return clientCredit
def getAllClientTelefono():
    clientTelefono= list()
    for val in cli.cliente:
        telefono=dict({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get("nombre_cliente"),
        "telefono": val.get("telefono")
        })
        clientTelefono.append(telefono)
    return(clientTelefono)
def getAllNombreClienteEspañol():
    clienteEspañol=[]
    for val in cli.cliente:
        if(val.get("pais")=="Spain"):
            clienteEspañol.append(
                {
                "nombre_cliente": val.get("nombre_cliente"),
                "pais":val.get("pais")  
                }
            )
    return clienteEspañol
def menu():
    print("""
REPORTES DE LOS CLIENTES
1. Obtener todos los clientes (codigo y nombre)
2. Obtener un cliente por el codigo
3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad a la que pertenece (ejem: 3000.0 - San Francisco)
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