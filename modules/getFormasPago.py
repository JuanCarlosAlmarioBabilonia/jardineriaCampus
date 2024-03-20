import requests
def getAllPagos():
    pet=requests.get("http://154.38.171.54:5006/pagos")
    data=pet.json()
    return data
def getAllTipoP():
    pagop = []
    for val in getAllPagos():
        pagop.append(val.get("forma_pago"))
    return pagop