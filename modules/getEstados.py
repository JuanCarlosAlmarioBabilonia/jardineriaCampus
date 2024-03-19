import requests
def getAllEstado():
    pet=requests.get("http://172.16.103.26:5511")
    data=pet.json()
    return data
def getAllName():
    estado = []
    for val in getAllEstado():
        estado.append(val.get("estado"))
    return estado