import storage.pedido as pe
from datetime import datetime
def getEstadoPedido():
    estadoPedido=[]
    for val in pe.pedido:
        pedido = dict({
        "estado": val.get("estado"),
        })
        estadoPedido.append(pedido)
    return estadoPedido
import storage.pedido as pe
from datetime import datetime
def getAllPedidosEntregadosDespuesDeTiempo():
    pedidosEntregados=[]
    for val in pe.pedido:
        if(val.get("estado")=="Entregado") and (val.get("fecha_entrega")==None):
            val["fecha_entrega"]=val.get("fecha_esperada")
        if(val.get("estado")=="Entregado"):
            date_1="/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2="/".join(val.get("fecha_esperada").split("-")[::-1])
            start=datetime.strptime(date_1,"%d/%m/%Y")
            end=datetime.strptime(date_2,"%d/%m/%Y")
            dif=end.date()-start.date()
            if(dif.days<0):
                pedidosEntregados.append({
                    "codigo_de_pedido":val.get("codigo_pedido"),
                    "codigo_de_cliente":val.get("codigo_cliente"),
                    "fecha_esperada":val.get("fecha_esperada"),
                    "fecha_de_entrega":val.get("fecha_entrega")
                })
    return pedidosEntregados
def getAllPedidosRechazados():
    pedidosRechazados=[]
    for val in pe.pedido:
        if(val.get("fecha_pedido")>=("2009-01-01") and (val.get("fecha_pedido")<=("2009-12-31")) and (val.get("estado")==("Rechazado"))):
            pedidosRechazados.append(val)
    return pedidosRechazados
def getAllPedidosEntregadoAntesDeTiempo():
    pedidosAntes=[]
    for val in pe.pedido:
        if(val.get("estado")=="Entregado") and (val.get("fecha_entrega")==None):
            val["fecha_entrega"]=val.get("fecha_esperada")
        if(val.get("estado")=="Entregado"):
            date_1="/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2="/".join(val.get("fecha_esperada").split("-")[::-1])
            start=datetime.strptime(date_1,"%d/%m/%Y")
            end=datetime.strptime(date_2,"%d/%m/%Y")
            dif=end.date()-start.date()
            if(dif.days>=2):
                pedidosAntes.append({
                    "codigo_de_pedido":val.get("codigo_pedido"),
                    "codigo_de_cliente":val.get("codigo_cliente"),
                    "fecha_esperada":val.get("fecha_esperada"),
                    "fecha_de_entrega":val.get("fecha_entrega")
                })
    return pedidosAntes
def getAllPedidosEntEnEnero():
    pedidosEnero=[]
    for val in pe.pedido:
        fecha=val.get("fecha_entrega")
        if fecha:
            date_1="/".join(val.get("fecha_entrega").split("-")[::-1])
            start=datetime.strptime(date_1,"%d/%m/%Y")
            if(start.month==1) and val.get("estado")=="Entregado":
                pedidosEnero.append({
                    "codigo_de_pedido":val.get("codigo_pedido"),
                    "codigo_de_cliente":val.get("codigo_cliente"),
                    "fecha_de_entrega":val.get("fecha_entrega"),
                    "estado":val.get("estado")
                })
    return pedidosEnero




