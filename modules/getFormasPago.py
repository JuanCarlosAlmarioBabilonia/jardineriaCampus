import requests
def getAllPagos():
    pet=requests.get("http://172.16.100.133:5512")
    data=pet.json()
    return data
def getAllTipoP():
    pagop = []
    for val in getAllPagos():
        pagop.append(val.get("forma_pago"))
    return pagop