import storage.cliente as cli 
def getAllClientesName():
    clienteName = list()
    for val in cli.cliente:
        codigoName = dict({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get("nombre_cliente")
        })
        clienteName.append(codigoName)
    return clienteName
def getOneClientCodigo(codigo):
    for val in cli.cliente:
        if(val.get("codigo_cliente") == codigo):
            return{
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get("cliente_cliente")   
            } 
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.cliente:
        if(val.get("limite_credito") >= limiteCredit and val.get("ciudad") == ciudad):
            clienteCredic.append(val)
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