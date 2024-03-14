import modules.getClientes as clientes
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago
import modules.getProducto as producto
import modules.postProducto as postproducto
import os
def menuProducto():
    while True:
        os.system("clear")
        print("""
MENU DE PRODUCTOS
0. Regresar al menu principal
1. Obtener productos de una categoria ordenando su precio de venta y rectificando que su cantidad de stock sea superior
2. Guardar datos
              """)
        op=int(input("Seleccione una de las opciones: "))
        if(op==1):
            producto.menu()
        elif(op==2):
            postproducto.menu()
        elif(op==0):
            break
if(__name__ == "__main__"):
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
        op=int(input("Seleccione una de las opciones: "))
        if(op==1):
            clientes.menu()
        elif(op==2):
            oficina.menu()
        elif(op==3):
            empleado.menu()
        elif(op==4):
            pedido.menu()
        elif(op==5):
            pago.menu()
        elif(op==6):
            menuProducto()
        elif(op==0):
            break
