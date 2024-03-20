import requests
def getAllEstado():
    pet=requests.get("http://154.38.171.54:5007/pedidos")
    data=pet.json()
    return data
def getAllName():
    estado = []
    for val in getAllEstado():
        estado.append(val.get("estado"))
    return estado