import storage.pago as pa
from tabulate import tabulate
def getCodigoClientePago(): 
    codigoCliente=[]
    codigosVistos=set()
    for val in pa.pago:
        if (val.get("fecha_pago")>("2008-01-01") and val.get("fecha_pago")<("2008-12-31")):
            codigoClientes=val.get("codigo_cliente")
            if codigoClientes not in codigosVistos:
                codigoCliente.append({
                    "Codigo del cliente":val.get("codigo_cliente"),
                    "Fecha del pago":val.get("fecha_pago"),
                    "Total":val.get("total")
                })
                codigosVistos.add(codigoClientes)
    return codigoCliente
def getAllPagosPaypal():
    pagosPaypal=[]
    for val in pa.pago:
        if(val.get("fecha_pago")>=("2008-01-01") and (val.get("fecha_pago")<=("2008-12-31")) and val.get("forma_pago")==("PayPal")):
            pagosPaypal.append({
                "Codigo del cliente":val.get("codigo_cliente"),
                "Forma de pago":val.get("forma_pago"),
                "ID de la transaccion":val.get("id_transaccion"),
                "Fecha del pago":val.get("fecha_pago"),
                "Total":val.get("total")
            })
            pagos_2008_paypal_ordenados = sorted(pagosPaypal, key=lambda x: x["total"], reverse=True)
    return (pagos_2008_paypal_ordenados)
def getAllFormasPago(): 
    formasPago=[]
    formasPagoVistas=set()
    for val in pa.pago:
        formaDePago=val.get("forma_pago")
        if formaDePago not in formasPagoVistas:
            formasPago.append({
                "Formas de Pago": val.get("forma_pago"),
            })
            formasPagoVistas.add(formaDePago)
    return formasPago
def menu():
    print("""
REPORTES DE LOS PAGOS
1. Obtener todos los pagos realizados en 2008
2. Obtener todos los pagos realizados por PayPal
3. Obtener las diferentes formas de pago existentes
""")
    op=int(input("Seleccione una de las opciones: "))
    if(op==1):
        print(tabulate(getCodigoClientePago(),headers="keys",tablefmt="grid"))
    elif(op==2):
        print(tabulate(getAllPagosPaypal(),headers="keys",tablefmt="grid"))
    elif(op==3):
        print(tabulate(getAllFormasPago(),headers="keys",tablefmt="grid"))