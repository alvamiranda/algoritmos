from pila import Pila


pila = Pila()

misiones = [

    {'planeta_visitado': 'Marte', 'capturado': 'Han Solo', 'costo': 2000},
    {'planeta_visitado': 'Jupiter', 'capturado': 'Adam', 'costo': 34543},
    {'planeta_visitado': 'Tierra', 'capturado': 'Amy Philips', 'costo': 27675},
    {'planeta_visitado': 'Saturno', 'capturado': 'Tyler', 'costo': 2777},
]


for mision in misiones:
    pila.push(mision)

recaudacion=0
tamanio_pila = pila.size()

print("Planetas Visitados:")
for i in range(tamanio_pila):
    value = pila.pop()

    print(value['planeta_visitado'])

    recaudacion += value['costo']

    num_mision= i+1
    if value['capturado']== 'Han Solo':
        num_mision_capturado = num_mision
        nom_planeta_capturado = value['planeta_visitado']

print()
print('Recaudado:')
print(recaudacion)
print()
print(f"San Holo fue capturado en la mision {num_mision}, en el planeta {nom_planeta_capturado}.")