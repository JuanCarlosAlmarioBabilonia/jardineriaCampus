import requests
def getAllPuestos():
    pet=requests.get("http://154.38.171.54:5003/empleados")
    data=pet.json()
    return data
def getAllTipoPu():
    puesto = []
    for val in getAllPuestos():
        puesto.append(val.get("puesto"))
    return puesto