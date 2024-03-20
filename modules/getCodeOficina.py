import requests
def getAllCodeOf():
    pet=requests.get("http://154.38.171.54:5005/oficinas")
    data=pet.json()
    return data
def getAllNameOf():
    ofNombre = []
    for val in getAllCodeOf():
        ofNombre.append(val.get("codigo_oficina"))
    return ofNombre