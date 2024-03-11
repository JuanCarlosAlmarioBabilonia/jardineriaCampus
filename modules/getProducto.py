import storage.producto as pr
def getAllProductosOrnamentales(gama, stock):
    condiciones=[]
    for val in pr.producto:
        if(val.get("gama")==gama) and(val.get("precio_venta")<=stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price)
    return condiciones
