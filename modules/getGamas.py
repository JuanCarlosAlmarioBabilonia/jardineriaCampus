import requests
def getAllGama():
    pet=requests.get("http://154.38.171.54:5004/gama")
    data=pet.json()
    return data
def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre