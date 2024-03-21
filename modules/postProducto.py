import json
import requests
from tabulate import tabulate
import modules.getGamas as gG
import os
import re
import modules.getProducto as gP
from modules.updateProducto import menuActualizacionProducto
def postProducto():
    producto=dict()
    while True:
        try:
            if(not producto.get("codigo_producto")):
                codigo=input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{2,3}$',codigo)is not None):
                    data=(gP.getProductCodigo2(codigo))
                    if(data):
                        print(tabulate(data,headers="keys", tablefmt="grid"))
                        raise Exception("El producto ya existe")
                    else:
                        producto["codigo_producto"]=codigo
                else:
                    raise Exception("El codigo del producto no cumple con el estandar establecido")
                
            if(not producto.get("nombre")):
                nombre=input("Ingrese el nombre del producto: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre)is not None):
                    producto["nombre"]=nombre
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")
                
            if not producto.get("gama"):
                gama= input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
            if re.match(r'^[0-4]$', gama) is not None:  
                gamab = int(gama)
                gama = gG.getAllNombre()[gamab]
                producto["gama"] = gama
            else:
                raise Exception("La gama del producto no cumple con el estándar establecido")
            
            if(not producto.get("dimensiones")):
                dimensiones=input("Ingrese las dimensiones del producto: ")
                if(re.match(r'^[0-9]{2,3}-[0-9]{2,3}$',dimensiones)is not None):
                     producto["dimensiones"]=dimensiones
                else:
                    raise Exception("Las dimensiones del producto no cumplen con el estandar establecido")
                
            if(not producto.get("proveedor")):
                proveedor=input("Ingrese el proovedor del producto: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',proveedor)is not None):
                    producto["proveedor"]=proveedor
                else:
                    raise Exception("El proveedor del producto no cumple con el estandar establecido")
                
            if(not producto.get("descripcion")):
                descripcion=input("Ingrese la descripcion del producto: ")
                if(re.match(r'^([A-Za-z][a-z]*\s*)+$',descripcion)is not None):
                    producto["descripcion"]=descripcion
                else:
                    raise Exception("La descripcion del producto no cumple con el estandar establecido")  
                
            if(not producto.get("cantidad_en_stock")):
                cantidad_en_stock=input("Ingrese la cantidad en stock del producto: ")
                if(re.match(r'^[0-9]{2,3}$',cantidad_en_stock)is not None):
                    cantidad_en_stock= int(cantidad_en_stock)
                    producto["cantidad_en_stock"]=cantidad_en_stock
                else:
                    raise Exception("La cantidad en stock no cumple con el estandar establecido") 
                
            if(not producto.get("precio_venta")):
                precio_venta=input("Ingrese el precio de venta del producto: ")
                if(re.match(r'^[0-9]{2,3}$',precio_venta)is not None):
                    precio_venta= int(precio_venta)
                    producto["precio_venta"]=precio_venta
                else:
                    raise Exception("El precio de venta del producto no cumple con el estandar establecido")  

            if(not producto.get("precio_proveedor")):
                precio_proveedor=input("Ingrese el precio de venta del producto: ")
                if(re.match(r'^[0-9]{1,3}$',precio_proveedor)is not None):
                    precio_proveedor= int(precio_proveedor)
                    producto["precio_proveedor"]=precio_proveedor
                    break
                else:
                    raise Exception("El precio de venta del producto no cumple con el estandar establecido")     
                
        except Exception as error:
            print(error)
    pet=requests.post("http://154.38.171.54:/productos", data=json.dumps(producto))
    res=pet.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]
def deleteProducto(id):
    data=gP.getProductCodigo(id)
    if(len(data)):
        while True:
            try:
                print("""
¿DESEA ELIMINAR COMPLETAMENTE EL PRODUCTO?
1. Si
2. No
               """)
                afirm = (input("Selecione una de las opciones: "))
                if(re.match(r'^[1-2]$', afirm)is not None):
                        afirm=int(afirm)
                        if (afirm==1):
                            pet=requests.delete(f"http://154.38.171.54:5008/productos/{id}")
                            if(pet.status_code==204):
                                return[{"Mensaje": "El producto ha sido eliminado satisfactoriamente"}]
                            break
                        else:
                            return[{"Mensaje": "Eliminacion cancelada"}]
                        
                else:
                    raise Exception("El dato ingresado no esta comprendido entre los estandares solicitados")
            except Exception as error:
                print(error)
    else:
        return[{
            "message": "Producto no encontrado",
            "id": id
        }]  
def updateProducto(id):
    data=gP.getProductCodigo(id)
    if(len(data)):
            producto=dict()
            while True:
                try:
                    if(not producto.get("codigo_producto")):
                        codigo=input("Ingrese el codigo del producto: ")
                        if(re.match(r'^[A-Z]{2}-[0-9]{2,3}$',codigo)is not None):
                            data=(gP.getProductCodigo2(codigo))
                            if(data):
                                print(tabulate(data,headers="keys", tablefmt="grid"))
                                raise Exception("El producto ya existe")
                            else:
                                producto["codigo_producto"]=codigo
                        else:
                            raise Exception("El codigo del producto no cumple con el estandar establecido")
                        
                    if(not producto.get("nombre")):
                        nombre=input("Ingrese el nombre del producto: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre)is not None):
                            producto["nombre"]=nombre
                        else:
                            raise Exception("El nombre del producto no cumple con el estandar establecido")
                        
                    if not producto.get("gama"):
                        gama= input("Seleccione la gama del producto:\n" + "".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
                    if re.match(r'^[0-4]$', gama) is not None:  
                        gamab = int(gama)
                        gama = gG.getAllNombre()[gamab]
                        producto["gama"] = gama
                    else:
                        raise Exception("La gama del producto no cumple con el estándar establecido")
                    
                    if(not producto.get("dimensiones")):
                        dimensiones=input("Ingrese las dimensiones del producto: ")
                        if(re.match(r'^[0-9]{2,3}-[0-9]{2,3}$',dimensiones)is not None):
                            producto["dimensiones"]=dimensiones
                        else:
                            raise Exception("Las dimensiones del producto no cumplen con el estandar establecido")
                        
                    if(not producto.get("proveedor")):
                        proveedor=input("Ingrese el proovedor del producto: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',proveedor)is not None):
                            producto["proveedor"]=proveedor
                        else:
                            raise Exception("El proveedor del producto no cumple con el estandar establecido")
                        
                    if(not producto.get("descripcion")):
                        descripcion=input("Ingrese la descripcion del producto: ")
                        if(re.match(r'^([A-Za-z][a-z]*\s*)+$',descripcion)is not None):
                            producto["descripcion"]=descripcion
                        else:
                            raise Exception("La descripcion del producto no cumple con el estandar establecido")  
                        
                    if(not producto.get("cantidad_en_stock")):
                        cantidad_en_stock=input("Ingrese la cantidad en stock del producto: ")
                        if(re.match(r'^[0-9]{2,3}$',cantidad_en_stock)is not None):
                            cantidad_en_stock= int(cantidad_en_stock)
                            producto["cantidad_en_stock"]=cantidad_en_stock
                        else:
                            raise Exception("La cantidad en stock no cumple con el estandar establecido") 
                        
                    if(not producto.get("precio_venta")):
                        precio_venta=input("Ingrese el precio de venta del producto: ")
                        if(re.match(r'^[0-9]{2,3}$',precio_venta)is not None):
                            precio_venta= int(precio_venta)
                            producto["precio_venta"]=precio_venta
                        else:
                            raise Exception("El precio de venta del producto no cumple con el estandar establecido")  

                    if(not producto.get("precio_proveedor")):
                        precio_proveedor=input("Ingrese el precio de venta del producto: ")
                        if(re.match(r'^[0-9]{1,3}$',precio_proveedor)is not None):
                            precio_proveedor= int(precio_proveedor)
                            producto["precio_proveedor"]=precio_proveedor
                            break
                        else:
                            raise Exception("El precio de venta del producto no cumple con el estandar establecido")                    
                except Exception as error:
                    print(error)

            pet=requests.put(f"http://154.38.171.54:5008/productos/{id}", data=json.dumps(producto))
            res=pet.json()
            res["Mensaje"] = "Producto Guardado"
            return [res]
    else:
        return[{
            "message": "Producto no encontrado",
            "id": id
        }]

def menu():
    while True:
        os.system("clear")
        print("""
ADMINISTRACION DE PRODUCTOS
0.Atras
1.Guardar un producto
2.Eliminar un producto
3.Actualizar un producto 
               """)
        op = (input("Selecione una de las opciones: "))
        if(re.match(r'^[0-3]$', op)is not None):
            op=int(op)
        if(op== 1):
            print(tabulate(postProducto(),tablefmt="grid"))
            input("Presione una tecla para continuar.....")
        elif(op==2):
            idProducto=int(input("Ingrese el id del producto que desea eliminar:"))
            print(tabulate(deleteProducto(idProducto),tablefmt="grid"))
            input("...")
        elif(op==3):
            idProducto=int(input("Ingrese el id del producto que desea actualizar:"))
            print(tabulate(updateProducto(idProducto),tablefmt="grid"))
            input("...")
        elif(op== 0):
            break