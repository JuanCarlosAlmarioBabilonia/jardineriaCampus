import storage.pago as pa
def getCodigoClientePago():
    codigoCliente=[]
    for val in pa.pago:
        if (val.get("fecha_pago")>("2008-01-01") and val.get("fecha_pago")<("2008-12-31") and val.get("codigo_cliente")!=("codigo_cliente")):
            codigoCliente.append({
                "codigo_cliente":val.get("codigo_cliente"),
                "fecha_pago":val.get("fecha_pago")
            })
    return codigoCliente
def getAllPagosPaypal():
    pagosPaypal=[]
    for val in pa.pago:
        if(val.get("fecha_pago")>=("2008-01-01") and (val.get("fecha_pago")<=("2008-12-31")) and val.get("forma_pago")==("PayPal")):
            pagosPaypal.append(val)
            pagos_2008_paypal_ordenados = sorted(pagosPaypal, key=lambda x: x["total"], reverse=True)
    return (pagos_2008_paypal_ordenados)
def getAllFormasPago():
    formasPago=[]
    for val in pa.pago:
        formapago=dict({
        "pago": val.get("forma_pago"),
        })
        formasPago.append(formapago)
    return formasPago