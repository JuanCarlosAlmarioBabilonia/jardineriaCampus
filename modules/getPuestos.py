import requests
def getAllPuestos():
    pet=requests.get("http://192.168.20.37:5513")
    data=pet.json()
    return data
def getAllTipoPu():
    puesto = []
    for val in getAllPuestos():
        puesto.append(val.get("puesto"))
    return puesto