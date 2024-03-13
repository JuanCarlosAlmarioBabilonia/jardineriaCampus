import json
def postProducto(producto):
    import requests
    pet=requests.get("http://172.16.100.133:5503")
    res=pet.json()
    return res