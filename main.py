import json
import generador as ge

datos_importados = ge.datos_generados

for i in range(len(datos_importados)):
    print(datos_importados[i])


with open('datos.json','r') as file:
    datos = json.load(file)
# print(json.dumps(datos, indent=4))
