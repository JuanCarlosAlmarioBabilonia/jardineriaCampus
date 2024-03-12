from tabulate import tabulate
import modules.getClientes as clientes
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago
import modules.getProducto as producto
def menu():
    while True:
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
            producto.menu()
        elif(op==0):
            break
menu()