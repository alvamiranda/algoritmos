from lista import Lista
from cola import Cola



class Personaje():
    def __init__(self, nombre_super, nombre_per, grupo, anio_ap):
        self.nombre_super = nombre_super
        self.nombre_per = nombre_per
        self.grupo = grupo
        self.anio_ap = anio_ap

    def __str__(self):
        return f"{self.nombre_super} - {self.nombre_per} - {self.grupo} - {self.anio_ap}"
    

lista = Lista()
cola= Cola()

data = [
    {'nombre_super': 'Capitana Marvel', 'nombre_per': 'Carol Danvers', 'grupo': 'a', 'anio_ap': 2010},
    {'nombre_super': 'Star Lord', 'nombre_per': 'Peter Quill', 'grupo': 'Guardianes de la galaxia', 'anio_ap': 1995},
    {'nombre_super': 'Adam Warlock', 'nombre_per': 'Adam Warlock', 'grupo': 'Guardianes de la galaxia', 'anio_ap': 1995},
    {'nombre_super': 'Mujer invisible', 'nombre_per': 'Susan Storm', 'grupo': 'Los 4 fantasticos', 'anio_ap': 1930},
    {'nombre_super': 'Antorcha humana', 'nombre_per': 'John Storm', 'grupo': 'Los 4 fantasticos', 'anio_ap': 1980},
    {'nombre_super': 'Vlack Widow', 'nombre_per': 'Natasha Romanoff', 'grupo': 'Avengers', 'anio_ap': 1980},
    {'nombre_super': 'Black Cat', 'nombre_per': 'Felicia Hardy', 'grupo': 'Avengers', 'anio_ap': 1922},
    {'nombre_super': 'Hulk', 'nombre_per': 'Paul Harrison', 'grupo': 'Avengers', 'anio_ap': 2022},
    {'nombre_super': 'Black Cat', 'nombre_per': 'Felicia Hardy', 'grupo': 'Avengers', 'anio_ap': 1912},
    {'nombre_super': 'Superman', 'nombre_per': 'Clark Kent', 'grupo': 'Avengers', 'anio_ap': 1954},
    {'nombre_super': 'Batman', 'nombre_per': 'Bruce Wayne', 'grupo': 'Avengers', 'anio_ap': 1922},
    {'nombre_super': 'Spider-Man', 'nombre_per': 'Peter Parker', 'grupo': 'Avengers', 'anio_ap': 1988},
    {'nombre_super': 'Wonder Woman', 'nombre_per': 'Diana Prince', 'grupo': 'Avengers', 'anio_ap': 1933},
    {'nombre_super': 'Iron Man', 'nombre_per': 'Tony Stark', 'grupo': 'Avengers', 'anio_ap': 1955},
    {'nombre_super': 'Capitan America', 'nombre_per': 'Steve Rogers', 'grupo': 'Avengers', 'anio_ap': 1977},
    {'nombre_super': 'Flash', 'nombre_per': 'Bruce Banner', 'grupo': 'Avengers', 'anio_ap': 1980},
    {'nombre_super': 'Linterna Verde', 'nombre_per': 'Thor Odinson', 'grupo': 'Avengers', 'anio_ap': 2000},
    {'nombre_super': 'Wolverine', 'nombre_per': 'Logan', 'grupo': 'Avengers', 'anio_ap': 1922},
    {'nombre_super': 'Pantera Negra', 'nombre_per': 'Arthur Curry', 'grupo': 'Avengers', 'anio_ap': 1965},
    {'nombre_super': 'Aquaman', 'nombre_per': 'Challa', 'grupo': 'Avengers', 'anio_ap': 1923},
]

for personaje in data:
    lista.insert(Personaje(personaje['nombre_super'], personaje['nombre_per'], personaje['grupo'], personaje['anio_ap']), 'nombre_super')

#a

pos = lista.search('Capitana Marvel', 'nombre_super')


print('#a')
if pos != None:
    value = lista.get_element_by_index(pos)
    print(f"Nombre de personaje de capitana marvel: {value.nombre_per}")
else: print('No se encuentra')




print()
print('#b')

for i in range(lista.size()):
    value = lista.get_element_by_index(i)
    if value.grupo == 'Guardianes de la galaxia':
        cola.arrive(value.grupo)

print(f"Son {cola.size()} superheroes")

print()
print('#c')
lista.order_by('nombre_per', True)

for i in range(lista.size()):
    value = lista.get_element_by_index(i)
    if value.grupo == 'Guardianes de la galaxia':
        print(value)

print()

for i in range(lista.size()):
    value = lista.get_element_by_index(i)
    if value.grupo == 'Los 4 fantasticos':
        print(value)

print()
print('#d')

for i in range(lista.size()):
    value = lista.get_element_by_index(i)
    if value.anio_ap > 1960:
        print(value)

print()
print('#g')

data_2= [
    {'nombre_super': 'Black Cat', 'nombre_per': 'Felicia Hardy', 'grupo': 'Avengers', 'anio_ap': 1980},
    {'nombre_super': 'Hulk', 'nombre_per': 'Paul Harrison', 'grupo': 'Avengers', 'anio_ap': 1980},
    {'nombre_super': 'Loki', 'nombre_per': 'Tom Hiddleston', 'grupo': 'Avengers', 'anio_ap': 1980},
    {'nombre_super': 'Rocket Racoon', 'nombre_per': 'Rocket Raccoon', 'grupo': 'Guardianes de la galaxia', 'anio_ap': 1980}
    ]


lista_aux = Lista()

for personaje in data_2:
    lista_aux.insert(Personaje(personaje['nombre_super'], personaje['nombre_per'], personaje['grupo'], personaje['anio_ap']), 'nombre_super')


for i in range(lista_aux.size()):
    value = lista_aux.get_element_by_index(i)
    
    if lista.search(value.nombre_super, 'nombre_super') is None:
        lista.insert(value, 'nombre_super')


print()
print('#h')

for i in range(lista.size()):
    value = lista.get_element_by_index(i)
    if value.nombre_super[0] == 'C' or value.nombre_super[0] == 'P' or value.nombre_super[0] == 'S':
        print(value)
