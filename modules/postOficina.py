import json
import requests
from tabulate import tabulate
import os
import re
import modules.getOficina as gO
def postOficina():
    oficina=dict()
    while True:
        try:
            if(not oficina.get("codigo_oficina")):
                codigo_oficina=input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{3}-[A-Z]{2}$',codigo_oficina)is not None):
                    data=(gO.getOficinaCodigo(codigo_oficina))
                if(data):
                    print(tabulate(data,headers="keys", tablefmt="grid"))
                    raise Exception("La oficina ya existe")
                else:
                    oficina["codigo_oficina"]=codigo_oficina
            else:
                raise Exception("El codigo de oficina no cumple con el estandar establecido")
            
            if(not oficina.get("ciudad")):
                ciudad=input("Ingrese la ciudad de la oficina: ")
            if(re.match(r'^([A-Za-z][a-z]*\s*)+$',ciudad)is not None):
                oficina["ciudad"]=ciudad
            else:
                raise Exception("La ciudad de la oficina no cumple con el estandar establecido")  
                
            if(not oficina.get("region")):
                region=input("Ingrese la region de la oficina: ")
            if(re.match(r'^([A-Za-z][a-z]*\s*)+$',region)is not None):
                oficina["region"]=region
            else:
                    raise Exception("La region de la oficina no cumple con el estandar establecido")  
            
            if(not oficina.get("pais")):
                pais=input("Ingrese el pais de la oficina: ")
            if(re.match(r'^([A-Za-z][a-z]*\s*)+$',pais)is not None):
                    oficina["pais"]=pais
            else:
                raise Exception("El pais de la oficina no cumple con el estandar establecido")
            
            if(not oficina.get("codigo_postal")):
                codigo_postal=input("Ingrese su codigo postal: ")
            if(re.match(r'^[0-9]{5}$',codigo_postal)is not None):
                    codigo_postal= int(codigo_postal)
                    oficina["codigo_postal"]=codigo_postal
            else:
                raise Exception("El codigo postal de la oficina no cumple con el estandar establecido")
            
            if(not oficina.get("telefono")):
                telefono=input("Ingrese su telefono: ")
            if(re.match(r'^[0-9]{10}$',telefono)is not None):
                    telefono= int(telefono)
                    oficina["telefono"]=telefono
            else:
                raise Exception("El telefono de la oficina no cumple con el estandar establecido")
            
            if(not oficina.get("linea_direccion1")):
                linea_direccion1=input("Ingrese su direccion principal: ")
            if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion1)is not None):
                    oficina["linea_direccion1"]=linea_direccion1
            else:
                raise Exception("Su linea de direccion principal no cumple con el estandar establecido")   
                
            if(not oficina.get("linea_direccion2")):
                linea_direccion2=input("Ingrese su direccion principal: ")
            if(re.match(r'^[0-9A-Za-z\s]+$',linea_direccion2)is not None):
                oficina["linea_direccion2"]=linea_direccion2
                break
            else:
                raise Exception("Su linea de direccion secundaria no cumple con el estandar establecido")   
        except Exception as error:
            print(error)
    pet=requests.post("http://172.16.100.125:5509", data=json.dumps(oficina))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def deleteOficina(id):
    data=gO.getOficinaCodigo(id)
    if(len(data)):
        while True:
            try:
                print("""
¿DESEA ELIMINAR COMPLETAMENTE LA OFICINA?
1. Si
2. No
               """)
                afirm = input("Selecione una de las opciones: ")
                if(re.match(r'^[1-2]$', afirm)is not None):
                        afirm=int(afirm)
                        if (afirm==1):
                            pet=requests.delete(f"http://172.16.100.125:5509/oficina/{id}")
                            if(pet.status_code==204):
                                return[{"Mensaje": "El cliente ha sido eliminado satisfactoriamente"}]
                            break
                        else:
                            return[{"Mensaje": "Eliminacion cancelada"}]
                        
                else:
                    raise Exception("El dato ingresado no esta comprendido entre los estandares solicitados")
            except Exception as error:
                print(error)
    else:
        return{
            "Body":[{
            "Mensaje":"El producto no ha sido encontrado",
            "ID":id
            }],
            "Status":400
        }
def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE OFICINAS
0. Atras
1. Guardar una oficina
2. Eliminar una oficina
              """)
        op = (input("Selecione una de las opciones: "))
        if(re.match(r'^[0-2]$', op)is not None):
            op=int(op)
        if(op==1):
            print(tabulate(postOficina(),tablefmt="grid"))
            input("Precione una tecla para continuar.....")
        elif(op==2):
            idProducto=int(input("Ingrese el id de la oficina que desea eliminar:"))
            print(tabulate(deleteOficina(idProducto),tablefmt="grid"))
            input("...")
        elif(op== 0):
            break