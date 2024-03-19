import requests
def getAllPagos():
    pet=requests.get("http://192.168.20.37:5512")
    data=pet.json()
    return data
def getAllTipoP():
    pagop = []
    for val in getAllPagos():
        pagop.append(val.get("forma_pago"))
    return pagop