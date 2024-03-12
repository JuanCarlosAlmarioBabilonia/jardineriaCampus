import storage.empleado as em
from tabulate import tabulate
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmp=[]
    for val in em.empleado:
        if(val.get("codigo_jefe")==codigo):
            nombreApellidoEmp.append({
                "Codigo del jefe":val.get("codigo_jefe"),
                "Nombre":val.get("nombre"),
                "Apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
                "Email":val.get("email"),
                "Codigo de la oficina":val.get("codigo_oficina")         
            })
    return nombreApellidoEmp
def getAllNombreApellidoEmailJefe2():
    nombreApellidoEmail2=[]
    for val in em.empleado:
        if(val.get("codigo_jefe")==None):
            nombreApellidoEmail2.append({
            "Nombre":val.get("nombre"),
            "Apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
            "Email":val.get("email"), 
            "Puesto":val.get("puesto"),                 
        })
    return nombreApellidoEmail2
def getAllNombreApellidoPuestoEmNoRep():
    nombreApellidoPuesto=[]
    for val in em.empleado:
        if(val.get("puesto")!=("Representante Ventas")):
            nombreApellidoPuesto.append({
            "Nombre":val.get("nombre"),
            "Apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
            "Puesto":val.get("puesto"),                 
        })
    return nombreApellidoPuesto
def getAllExtensionEmailEmp():
    exEm=[]
    for val in em.empleado:
        exEm.append({
            "Nombre":val.get("nombre"),
            "Apellidos":f"{val.get('apellido1')} {val.get('apellido2')}",
            "Email":val.get("email"), 
            "Extension":val.get("extension"),                 
        })
    return exEm
def menu():
    while True:
      print("""
REPORTES DE LOS EMPLEADOS
0. Regresar al menu principal
1. Obtener datos basicos de los empleados por el codigo ingresado
2. Obtener los datos basicos del Jefe
3. Obtener los datos basicos de los empleados cuyo puesto no sea Representante de Ventas
4. Obtener los emails y extensiones de todos los empleados
""")
      op=int(input("Seleccione una de las opciones: "))
      if(op==1):
        try:
            codigo=int(input("Ingrese el codigo: "))   
            print(tabulate(getAllNombreApellidoEmailJefe(codigo),headers="keys",tablefmt="grid"))
        except KeyboardInterrupt:
           return menu()
      elif(op==2):
        print(tabulate(getAllNombreApellidoEmailJefe2(),headers="keys",tablefmt="grid"))
      elif(op==3):
        print(tabulate(getAllNombreApellidoPuestoEmNoRep(),headers="keys",tablefmt="grid"))
      elif(op==4):
        print(tabulate(getAllExtensionEmailEmp(),headers="keys",tablefmt="grid"))
      elif(op==0):
          break 