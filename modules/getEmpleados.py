import storage.empleado as em
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail=[]
    for val in em.empleado:
        if(val.get("codigo_jefe")==codigo):
            nombreApellidoEmail.append(
                {
                    "nombre":val.get("nombre"),
                    "apellido1":val.get("apellido1"),
                    "apellido2":val.get("apellido2"),
                    "email":val.get("email"),
                    "jefe":val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail

def getAllNombreApellidoEmailJefe2():
    nombreApellidoEmail=[]
    for val in em.empleado:
        if(val.get("codigo_jefe")==None):
            nombreApellidoEmail.append(
                {
                    "puesto":val.get("puesto"),
                    "nombre":val.get("nombre"),
                    "apellido1":val.get("apellido1"),
                    "apellido2":val.get("apellido2"),
                    "email":val.get("email"),                  
                }
            )
    return nombreApellidoEmail

def getAllNombreApellidoPuestoEmNoRep():
    nombreApellidoPuesto=[]
    for val in em.empleado:
        if(val.get("puesto")!=("Representante Ventas")):
            nombreApellidoPuesto.append(
                {
                    "nombre":val.get("nombre"),
                    "apellido1":val.get("apellido1"),
                    "apellido2":val.get("apellido2"),
                    "puesto":val.get("puesto")
                } 
            )
    return nombreApellidoPuesto