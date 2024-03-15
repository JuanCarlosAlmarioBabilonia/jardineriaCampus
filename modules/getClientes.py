#import storage.cliente as cli
#import storage.empleado as em
#import storage.pago as pa
import os
import requests
from tabulate import tabulate
def getAllDataCli():
    pet=requests.get("http://192.168.20.37:5506")
    data=pet.json()
    return data
def getAllDataEmp():
    pet=requests.get("http://192.168.20.37:5507")
    data=pet.json()
    return data
def getAllDataPa():
    pet=requests.get("http://192.168.20.37:5508")
    data=pet.json()
    return data
def getAllClientesName():
    clienteName = []
    for val in getAllDataCli():
        clienteName.append ({
        "Codigo": val.get("codigo_cliente"),
        "Nombre del Cliente": val.get("nombre_cliente")
        })
    return clienteName
def getOneClientCodigo(codigo):
    for val in getAllDataCli():
        if(val.get("codigo_cliente") == codigo):
            return[{
        "Codigo del Cliente": val.get("codigo_cliente"),
        "Nombre del Cliente": val.get("nombre_cliente")   
            }]
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredic = []
    for val in getAllDataCli():
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
    clientZone = []
    for val in getAllDataCli():
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
    clientCodigoPostal= []
    for val in getAllDataCli():
        clientCodigoPostal.append({
        "Codigo del cliente": val.get("codigo_cliente"),
        "Nombre del cliente": val.get("nombre_cliente"),
        "Nombre del contacto":val.get("nombre_contacto"),
        "Apellido del contacto":val.get("apellido_contacto"),
        "Codigo postal": val.get("codigo_postal")
        })
    return(clientCodigoPostal)
def getAllClientCiudad(ciudad):
    clientCity = []
    for val in getAllDataCli():
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
    clientDireccion=[]
    for val in getAllDataCli():
        clientDireccion.append({
        "Codigo del cliente": val.get("codigo_cliente"),
        "Nombre del cliente": val.get("nombre_cliente"),
        "Nombre del contacto":val.get("nombre_contacto"),
        "Apellido del contacto":val.get("apellido_contacto"),
        "Direccion principal": val.get("linea_direccion1")
        })
    return(clientDireccion)
def getAllClientCreditEntre():
    clientCredit=[]
    for val in getAllDataCli():
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
    clientTelefono= []
    for val in getAllDataCli():
        clientTelefono.append({
        "Codigo del cliente":val.get("codigo_cliente"),
        "Nombre del cliente":val.get("nombre_cliente"),
        "Nombre del contacto":val.get("nombre_contacto"),
        "Apellido del contacto":val.get("apellido_contacto"),
        "Telefono": val.get("telefono")
        })
    return(clientTelefono)
def getAllNombreClienteEspañol():
    clienteEspañol=[]
    for val in getAllDataCli():
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
def getAllClienteCiudadRepVentas():
    clienteMadrid=[]
    for val in getAllDataCli():
        if((val.get("ciudad")=="Madrid") and (val.get("codigo_empleado_rep_ventas")== 11 or (val.get("codigo_empleado_rep_ventas")== 30))):
            clienteMadrid.append({
        "Codigo del cliente":val.get("codigo_cliente"),
        "Nombre del cliente":val.get("nombre_cliente"),
        "Nombre del contacto":val.get("nombre_contacto"),
        "Apellido del contacto":val.get("apellido_contacto"),
        "Ciudad": val.get("ciudad"),
        "Codigo del representante de ventas":val.get("codigo_empleado_rep_ventas")
        })
    return clienteMadrid
def getAllClientesReps():
    clientesRep=[]
    for x in getAllDataCli():
        for y in getAllDataEmp():
            if x.get("codigo_empleado_rep_ventas")==y.get("codigo_empleado"):
                clientesRep.append({
                    "Nombre del cliente": x.get("nombre_cliente"),
                    "Nombre del Representante de Ventas":y.get("nombre"),
                    "Apellidos del Representante de Ventas":f"{y.get('apellido1')} {y.get('apellido2')}" 
                })
    return clientesRep
def getAllClientesPagos():
    clientesPago=[]
    for x in getAllDataCli():
        for y in getAllDataEmp():
            for z in getAllDataPa():
                if x.get("codigo_cliente")==z.get("codigo_cliente") and x.get("codigo_empleado_rep_ventas")==y.get("codigo_empleado") :
                    clientesPago.append({
                        "Codigo del cliente":x.get("codigo_cliente"),
                        "Nombre del cliente": x.get("nombre_cliente"),
                        "Pago":z.get("total"),
                        "Nombre del Representante de Ventas":y.get("nombre"),
                        "Apellidos del Representante de Ventas":f"{y.get('apellido1')} {y.get('apellido2')}"                         
                    })
    return clientesPago
# def getAllClientesNoPagos():
#     clientesNoPago=[]
#     for a in cli.cliente:
#        pagos=False
#        for b in pa.pago:
#           if a.get("codigo_cliente")==b.get("codigo_cliente"):
#              pagos=True
#              break
#           if not pagos:
#              for c in em.empleado:
#                 if a.get("codigo_empleado_rep_ventas")==c.get("codigo_empleado"):
#                    if c.get("puesto")=="Representante Ventas":
#                       clientesNoPago.append({
#                          "Codigo del cliente": a.get("codigo_cliente"),
#                          "Nombre del cliente": a.get("nombre_cliente"),
#                          "Puesto": c.get("puesto"),
#                          "Representante de ventas": c.get("nombre")
#                       })
#     return clientesNoPago
def menu():
    while True:
        print("""
REPORTES DE LOS CLIENTES
0. Regresar al menu principal
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
11. Obtener los clientes que son de Madrid y que el codigo de su representante de ventas sea 11 o 30
12. Obtener todos los clientes con su respectivo Representante de Ventas 
13. Obtener todos los clientes que hayan realizado pagos con su respectivo Representante de Ventas
14. Obtener todos los clientes que no hayan realizado pagos con su respectivo Representante de Ventas
""")
        op=int(input("Seleccione una de las opciones: "))
        if(op==1):
            print(tabulate(getAllClientesName(),headers="keys",tablefmt="grid"))
            print(...)
        elif(op==2):
            try:
               codigoCliente=int(input("Ingrese el codigo del cliente: "))
               print(tabulate(getOneClientCodigo(codigoCliente),headers="keys",tablefmt="grid"))
            except KeyboardInterrupt:
               return menu()         
        elif(op==3):
            try:
               limite=float(input("Ingrese el limite de credito de los clientes que desea visualizar: "))
               ciudad=input("Ingrese el nombre de la ciudad de la que desea filtrar los clientes: ")
               print(tabulate(getAllClientCreditoCiudad(limite,ciudad),headers="keys",tablefmt="grid"))
            except KeyboardInterrupt:
               return menu()              
        elif(op==4):
            try:
               pais=input("Ingrese el pais del cliente con mayuscula(s) inicial(es): ")
               region=input("Ingrese la region del cliente con mayuscula(s) inicial(es): ")
               ciudad=input("Ingrese la ciudad del cliente con mayuscula(s) inicial(es): ")
               print(tabulate(getAllClientPaisRegionCiudad(pais,region,ciudad),headers="keys",tablefmt="grid"))
            except KeyboardInterrupt:
               return menu()
        elif(op==5):
         print(tabulate(getAllClientCodigoPostal(),headers="keys",tablefmt="grid"))
        elif(op==6):
            try:
                ciudad=input("Ingrese la ciudad con mayuscula(s) inicial(es): ")
                print(tabulate(getAllClientCiudad(ciudad),headers="keys",tablefmt="grid"))
            except KeyboardInterrupt:
                return menu()
        elif(op==7):
         print(tabulate(getAllClientDireccion(),headers="keys",tablefmt="grid"))
        elif(op==8):
         print(tabulate(getAllClientCreditEntre(),headers="keys",tablefmt="grid"))
        elif(op==9):
         print(tabulate(getAllClientCreditEntre(),headers="keys",tablefmt="grid"))
        elif(op==10):
         print(tabulate(getAllNombreClienteEspañol(),headers="keys",tablefmt="grid"))
        elif(op==11):
         print(tabulate(getAllClienteCiudadRepVentas(),headers="keys",tablefmt="grid"))
        elif(op==12):
         print(tabulate(getAllClientesReps(),headers="keys",tablefmt="grid")) 
        elif(op==13):
         print(tabulate(getAllClientesPagos(),headers="keys",tablefmt="grid")) 
        # elif(op==14):
        #  print(tabulate(getAllClientesNoPagos(),headers="keys",tablefmt="grid"))   
        elif(op==0):
            break
