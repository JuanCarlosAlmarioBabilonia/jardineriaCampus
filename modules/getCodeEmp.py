import requests
def getAllCodes():
    pet=requests.get("http://172.16.103.37:5514")
    data=pet.json()
    return data
def getAllCoEmp():
    codeEmpleado = []
    for val in getAllCodes():
        codeEmpleado.append(val.get("codigo_empleado"))
    return codeEmpleado