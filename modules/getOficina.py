import storage.oficina as of
from tabulate import tabulate
def getAllCodigoCiudad():
    codigoCiudad=[]
    for val in of.oficina:
        codigoCiudad.append({
            "Codigo de la oficina":val.get("codigo_oficina"),
            "Ciudad":val.get("ciudad")
        })
    return codigoCiudad
def getAllCiudadTelefono(pais):
    ciudadTelefono=[]
    for val in of.oficina:
        if (val.get("pais")==pais):
            ciudadTelefono.append({
                "Codigo de la oficina":val.get("codigo_oficina"),
                "Telefono de la oficina":val.get("telefono"),
                "Ciudad":val.get("ciudad"),
                "Pais":val.get("pais")
            })
    return ciudadTelefono
def getAllDirecciones():
    direccion=[]
    for val in of.oficina:
        direccion.append({
                "Codigo de la oficina":val.get("codigo_oficina"),
                "Ciudad":val.get("ciudad"),
                "Pais":val.get("pais"),
                "Region":val.get("region"),
                "Direccion 1":val.get("linea_direccion1"),
                "Direccion 2":val.get("linea_direccion2")
            })
    return direccion   
def menu():
    while True:
     print("""
REPORTES DE LAS OFICINAS
0. Regresar al menu principal
1. Obtener los codigos de las todas oficinas y las ciudades de ubicacion
2. Obtener el telefono de todas las oficinas del pais ingresado
3. Obtener las direcciones de todas las oficinas
""")
     op=int(input("Seleccione una de las opciones: "))
     if(op==1):
        print(tabulate(getAllCodigoCiudad(),headers="keys",tablefmt="grid"))
     elif(op==2):
        pais=input("Ingrese el pais con mayuscula(s) inicial(es): ")
        print(tabulate(getAllCiudadTelefono(pais),headers="keys",tablefmt="grid"))
     elif(op==3):
        print(tabulate(getAllDirecciones(),headers="keys",tablefmt="grid"))
     elif (op==0):
        break