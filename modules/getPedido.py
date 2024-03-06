import storage.pedido as pe
def getEstadoPedido():
    estadoPedido=[]
    for val in pe.pedido:
        pedido = dict({
        "estado": val.get("estado"),
        })
        estadoPedido.append(pedido)
    return estadoPedido
