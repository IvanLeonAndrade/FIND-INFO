import json
from faker import Faker
import random


fake = Faker()

def generar_ip_aleatoria():
    #Direcciónes IP aleatorias
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generar_ius_aleatorio():
    #IUS aleatorios
    return f"{fake.bothify(text='???###')}"

def generar_datos(n):
    #Genera n grupos de datos
    datos = []
    for _ in range(n):
        datos.append({
            "IP": generar_ip_aleatoria(),
            "IUS": generar_ius_aleatorio(),
            "Razon Social": fake.company()
        })
    return datos

# Cantidad de grupo de datos
cantidad_grupos = int(input('Ingrese la cantidad de grupo de datsos a generar: '))
datos_generados = generar_datos(cantidad_grupos)

with open('datos.json', 'w') as file:
    json.dump(datos_generados, file, indent=4)



