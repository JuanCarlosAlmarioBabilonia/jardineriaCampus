import requests
def getAllCodes():
    pet=requests.get("http://154.38.171.54:5003/empleados")
    data=pet.json()
    return data
def getAllCoEmp():
    codeEmpleado = []
    for val in getAllCodes():
        codeEmpleado.append(val.get("codigo_empleado"))
    return codeEmpleado