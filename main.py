import modules.getClientes as clientes
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago
import modules.getProducto as pr
import modules.postProducto as postproducto
import modules.postCliente as postCliente
import modules.postEmpleados as postEmpleado
import modules.postPagos as postPagos
import modules.postOficina as postOficina
import modules.postPedido as postPedido
import os
import re
import json
import tabulate
import requests

def menuProducto():
    while True:
        os.system("clear")
        print("""
MENU DE PRODUCTOS
0. Regresar al menu principal
1. Redireccionar a los filtros
2. Guardar datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-2]$', op)is not None):
            op=int(op)
        if(op==1):
            pr.menu()
        if(op==2):
            postproducto.menu()
        elif(op==0):
            break

def menuCliente():
    while True:
        os.system("clear")
        print("""
MENU DE CLIENTES
0. Regresar al menu principal
1. Redireccionar a los filtros
2. Guardar datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-2]$', op)is not None):
            op=int(op)
        if(op==1):
            clientes.menu()
        elif(op==2):
           postCliente.menu()
        elif(op==0):
            break

def menuEmpleado():
    while True:
        os.system("clear")
        print("""
MENU DE EMPLEADOS
0. Regresar al menu principal
1. Redireccionar a los filtros
2. Guardar datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-2]$', op)is not None):
            op=int(op)
        if(op==1):
            empleado.menu()
        elif(op==2):
           postEmpleado.menu()
        elif(op==0):
            break
def menuPagos():
    while True:
        os.system("clear")
        print("""
MENU DE PAGOS
0. Regresar al menu principal
1. Redireccionar a los filtros
2. Guardar datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-2]$', op)is not None):
            op=int(op)
        if(op==1):
            pago.menu()
        elif(op==2):
           postPagos.menu()
        elif(op==0):
            break
def menuOficina():
    while True:
        os.system("clear")
        print("""
MENU DE OFICINA
0. Regresar al menu principal
1. Redireccionar a los filtros
2. Guardar datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-2]$', op)is not None):
            op=int(op)
        if(op==1):
            oficina.menu()
        elif(op==2):
           postOficina.menu()
        elif(op==0):
            break
def menuPedidos():
    while True:
        os.system("clear")
        print("""
MENU DE PEDIDOS
0. Regresar al menu principal
1. Redireccionar a los filtros
2. Guardar datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-2]$', op)is not None):
            op=int(op)
        if(op==1):
            pedido.menu()
        elif(op==2):
           postPedido.menu()
        elif(op==0):
            break  
if(__name__ == "__main__"):
# with open("storage/pedido.json", "r") as f:
#     fichero = f.read()
#     data = json.loads(fichero)
#     for i, val in enumerate(data):
#         data[i]["id"] = (i+1)
#     data = json.dumps(data, indent=4).encode("utf-8")
# with open("storage/pedido.json", "wb+") as f1:
#     f1.write(data)
#     f1.close()
    while True:
        os.system("clear")
        print("""
MENU PRINCIPAL
0. Salir
1. Cliente
2. Oficina
3. Empleados
4. Pedidos
5. Pagos
6. Productos
 """)
        try:
            op=int(input("Seleccione una de las opciones: "))
            if(op==1):
                menuCliente()
            elif(op==2):
                menuOficina()
            elif(op==3):
                menuEmpleado()
            elif(op==4):
                menuPedidos()
            elif(op==5):
                menuPagos()
            elif(op==6):
               menuProducto()
            elif(op==0):
               break
        except ValueError:
            print("Error generado")

def menuActualizacionProducto():
    while True:
        os.system("clear")
        print("""
MENU DE ACTUALIZACION
1. Actualizar el codigo del producto
2. Actualizar el nombre del producto
3. Actualizar la gama del producto
4. Actualizar las dimensiones
5. Actualizar el proveedor del producto
6. Actualizar la descripcion del producto
7. Actualizar la cantidad en stock del producto
8. Actualizar el precio de venta del producto
9. Actualizar el precio del proveedor del producto
10. Actualizar todos los datos
              """)
        op=(input("Seleccione una de las opciones: "))
        if(re.match(r'[0-10]$', op)is not None):
            op=int(op)
        if(op==1):
                codigo=input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{2,3}$',codigo)is not None):
                    data=(pr.getProductCodigo2(codigo))
                if(data):
                    print(tabulate(data,headers="keys", tablefmt="grid"))
                    raise Exception("El producto ya existe")
                else:
                    pr["codigo_producto"]=codigo
        else:
            raise Exception("El codigo del producto no cumple con el estandar establecido")
        pet=requests.put(f"http://154.38.171.54:5008/productos/{id}", data=json.dumps(producto))
        res=pet.json()
        res["Mensaje"] = "Producto Guardado"
        return [res]
    # else:
        # return[{
        #      "message": "Producto no encontrado",
        #      "id": id
        #  }]
        # if(op==2):
        #         nombre=input("Ingrese el nombre del producto: ")
        #         if(re.match(r'^([A-Za-z][a-z]*\s*)+$',nombre)is not None):
        #             producto["nombre"]=nombre
        #         else:
        #             raise Exception("El nombre del producto no cumple con el estandar establecido")
        # elif(op==0):
        #     break  
    