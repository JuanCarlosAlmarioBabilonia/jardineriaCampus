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