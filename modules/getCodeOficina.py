import requests
def getAllCodeOf():
    pet=requests.get("http://172.16.100.133:5515")
    data=pet.json()
    return data
def getAllNameOf():
    ofNombre = []
    for val in getAllCodeOf():
        ofNombre.append(val.get("codigo_oficina"))
    return ofNombre