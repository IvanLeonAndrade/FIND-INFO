'''
    Este fichero simula ser NETBOX quien envia los datos. Para eso genera
    n cantidad de grupos y los guarda en un json. Luego el programa principal
    recibe el JSON.
'''
import json
from faker import Faker
import random
from datetime import datetime


fake = Faker()

def generar_ip_aleatoria():
    #Direcciónes IP aleatorias
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generar_ius_aleatorio():
    #IUS aleatorios
    return f"{fake.bothify(text='???###')}"

def generar_fecha_aleatoria():
    # Genera una fecha aleatoria en un rango específico (por ejemplo, entre 2000 y 2023)
    start_date = datetime.strptime('2000-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2023-12-31', '%Y-%m-%d')
    return fake.date_between(start_date=start_date, end_date=end_date)

def generar_datos(n):
    #Genera n grupos de datos
    datos = []
    for _ in range(n):
        datos.append({
            "IP": generar_ip_aleatoria(),
            "IUS": generar_ius_aleatorio(),
            "Razon Social": fake.company(),
            "Fecha": str(generar_fecha_aleatoria())
        })
    return datos

# Cantidad de grupo de datos
cantidad_grupos = int(input('Ingrese la cantidad de grupo de datsos a generar: '))
datos_generados = generar_datos(cantidad_grupos)

with open('datos.json', 'w') as file:
    json.dump(datos_generados, file, indent=4)



