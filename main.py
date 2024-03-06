from tabulate import tabulate
import modules.getClientes as clientes
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago
print (tabulate(pago.getCodigoClientePago()))