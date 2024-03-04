import modules.getClientes as clientes
from tabulate import tabulate
print (tabulate(clientes.getAllClientTelefono()))