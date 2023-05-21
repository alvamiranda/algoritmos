from pila import Pila

personajes=[
    {'nombre': 'Rocket Raccoon', 'cantidad': 5},
    {'nombre': 'Groot', 'cantidad': 6},
    {'nombre': 'Black Widow', 'cantidad': 4}
]

particip=[]
personajes_CDG=[]

pila_1=Pila()

for personaje in personajes:
    pila_1.push(personaje)

contador=1
while pila_1.size()>0:

    valor=pila_1.pop()
    if valor['nombre']== 'Rocket Raccoon':
        pos_rocket= contador
    if valor['nombre']== 'Groot':
        pos_groot= contador
    
    if valor['cantidad'] > 5:
        particip.append(valor)
    
    if valor['nombre']== 'Black Widow':
        pelis_bw=valor['cantidad']

    
    if valor['nombre'][0]== 'G' or valor['nombre'][0]== 'D' or valor['nombre'][0]== 'G':
        personajes_CDG.append(valor)

    contador=contador+1

print(f'Rocket Raccoon se encuentra en la posicion {pos_rocket} y Groot en la posicion {pos_groot}')
print()

print('Los personajes que participaron en mas de 5 peliculas son: ')
for personaje in particip:
    print(f"{personaje['nombre']} ({personaje['cantidad']})")

print()
print(f"Black Widow participo en {pelis_bw} peliculas")

print()
print("Los personajes cuyos nombres empizan con C, D y G")

for personaje in personajes_CDG:
    print(personaje['nombre'])



