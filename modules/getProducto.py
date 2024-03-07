import storage.producto as pr
def getAllProductosOrnamentales():
    productosOrnamentales=[]
    for val in pr.producto:
        if ((val.get("gama")==("Ornamentales") and val.get("cantidad_en_stock")>100)):
            productosOrnamentales.append({
                "nombre":val.get("nombre"),
                "gama":val.get("gama"),
                "cantidad_en_stock":val.get("cantidad_en_stock"),
                "precio_venta":val.get("precio_venta")
        })
    return productosOrnamentales