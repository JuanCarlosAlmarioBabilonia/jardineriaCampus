import requests
def getAllEstado():
    pet=requests.get("http://192.168.20.37:5511")
    data=pet.json()
    return data
def getAllName():
    estado = []
    for val in getAllEstado():
        estado.append(val.get("estado"))
    return estado