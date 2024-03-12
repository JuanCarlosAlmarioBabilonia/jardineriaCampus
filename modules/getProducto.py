import storage.producto as pr
from tabulate import tabulate
def getAllProductosOrnamentales():
    condiciones=[]
    for val in pr.producto:
        if(val.get("gama")=="Ornamentales") and (val.get("cantidad_en_stock")>=100):
            condiciones.append({
                "Codigo del Producto":val.get("codigo_producto"),
                "Nombre":val.get("nombre"),  
                "Gama":val.get("gama"),  
                "Dimensiones":val.get("dimensiones"),  
                "Proveedor":val.get("proveedor"),  
                "Cantidad en stock":val.get("cantidad_en_stock"),  
                "Precio de venta":val.get("precio_venta"),  
                "Precio al proveedor":val.get("precio_proveedor")              
            })
            productos_ordenados = sorted(condiciones, key=lambda x: x["Precio de venta"], reverse=True)
    return productos_ordenados
def menu():
    while True:
        print("""
REPORTES DE LOS PRODUCTOS
0. Regresar al menu principal
1. Obtener productos de la gama Ornamentales con su cantidad en stock
""")
        op=int(input("Seleccione una de las opciones: "))
        if (op==1):
                print(tabulate(getAllProductosOrnamentales(),headers="keys",tablefmt="grid"))
        elif(op==0):
            break
