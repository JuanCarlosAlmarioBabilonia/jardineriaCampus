import requests
def getAllGama():
    pet=requests.get("http://172.16.103.37:5505")
    data=pet.json()
    return data
def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre