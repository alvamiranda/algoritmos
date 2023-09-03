from lista_lista import Lista
from random import randint

class Entrenador():
    
    def __init__(self, nombre, t_ganados=0, b_perdidas=0, b_ganadas=0):
        self.nombre=nombre
        self.t_ganados=t_ganados
        self.b_perdidas=b_perdidas
        self.b_ganadas=b_ganadas

    def __str__(self):
        return f"{self.nombre} - {self.t_ganados} - {self.b_perdidas} - {self.b_ganadas}"
    

class Pokemon():
    def __init__(self, nombre, nivel, tipo, subtipo=None):
        self.nombre=nombre
        self.nivel=nivel
        self.tipo=tipo
        self.subtipo=subtipo
    
    def __str__(self):
        return f"{self.nombre} - {self.nivel} - {self.tipo} - {self.subtipo}"
    

e1 = Entrenador('Juan', randint(0,10), randint(0,10), randint(0,10))
e2 = Entrenador('Jose', randint(0,10), 1, 20)
e3 = Entrenador('Maria', randint(0,10), randint(0,10), randint(0,10))

entrenadores= [e1, e2, e3]

lista_entrenadores = Lista()

for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

p1 = Pokemon('Pikachu', randint(0,20), 'electrico') 
p2= Pokemon('Wingull', randint(0,20), 'Veneno')
p3= Pokemon('Charmander', randint(0,20), 'Fuego', 'Planta')
p4= Pokemon('Tyrantrum', randint(0,20), 'Agua', 'Volador')
p5= Pokemon('Terrakion', randint(0,20), 'Tierra')

lista_pokemons = Lista()

pokemons= [p1, p2, p3, p4 , p5]

for pokemon in pokemons:
    lista_pokemons.insert(pokemon, 'nombre')
    num_entrenador = (randint(0, lista_entrenadores.size()-1))
    entrenador= lista_entrenadores.get_element_by_index(num_entrenador)
    entrenador[1].insert(pokemon, 'nombre')
    num_entrenador = (randint(0, lista_entrenadores.size()-1))
    entrenador= lista_entrenadores.get_element_by_index(num_entrenador)
    entrenador[1].insert(pokemon, 'nombre')

#a
def cant_pokemons(nombre):
    pos=lista_entrenadores.search(nombre, 'nombre')
    if pos is not None:
        value= lista_entrenadores.get_element_by_index(pos)
        entrenador, sublista= value[0], value[1] 
        print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')


cant_pokemons('Jose')

#b
for pos in range(lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.t_ganados>3:
        print(entrenador)

#c

max_t_ganados= 0
mayor_nivel=0

for pos in range(0, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.t_ganados>max_t_ganados:
        max_t_ganados= entrenador.t_ganados
        pos_mayor= pos

value = lista_entrenadores.get_element_by_index(pos_mayor)


entrenador, sublista = value[0], value[1]

for pos in range(0, sublista.size()):
    pokemon= sublista.get_element_by_index(pos)
    if (pokemon.nivel > mayor_nivel):
        pokemon_mayor_nivel = pokemon
        mayor_nivel = pokemon.nivel
    
print(f"el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados: {pokemon_mayor_nivel}")

#d

pos = lista_entrenadores.search('Maria', 'nombre')
value = lista_entrenadores.get_element_by_index(pos)

entrenador, sublista = value[0], value[1]

print()
print(f"Entrenador: {entrenador}")

print('Pokemons:')
for i in range(0, sublista.size()):
    print(sublista.get_element_by_index(i))

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
print()
print("los entrenadores que tienen Pokémons de tipo fuego y planta o agua/volador:")

for i in range(0, lista_entrenadores.size()):

    value= lista_entrenadores.get_element_by_index(i)

    entrenador, sublista = value[0], value[1]

    for pos in range(0, sublista.size()):  
        pokemon= sublista.get_element_by_index(pos)
        if ((pokemon.tipo == 'Fuego') and (pokemon.subtipo == 'Planta')):
            print(entrenador)
        if ((pokemon.tipo == 'Agua') and (pokemon.subtipo == 'Volador')):
            print(entrenador)

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

print()
print("los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %:")
for i in range(0, lista_entrenadores.size()):

    value= lista_entrenadores.get_element_by_index(i)

    entrenador = value[0]

    tot_batallas= entrenador.b_ganadas + entrenador.b_perdidas
    porcentaje_ganadas= (entrenador.b_ganadas * 100) / tot_batallas

    if porcentaje_ganadas > 79:
        print(entrenador)

print()

# g. el promedio de nivel de los Pokémons de un determinado entrenador;

pos = lista_entrenadores.search('Maria', 'nombre')
value = lista_entrenadores.get_element_by_index(pos)

entrenador, sublista = value[0], value[1]

for pos in range(0, sublista.size()):  
    pokemon= sublista.get_element_by_index(pos)
    pokemon_suma =+ pokemon.nivel

promedio_pokemon= (pokemon_suma)/sublista.size()

print(f'El promedio de nivel de los pokemons de {entrenador} es:')
print(promedio_pokemon)

#h. determinar cuántos entrenadores tienen a un determinado Pokémon;

for i in range(0, lista_entrenadores.size()):

    value= lista_entrenadores.get_element_by_index(i)

    entrenador, sublista = value[0], value[1]

    pos=sublista.search('Pikachu', 'nombre')
    
    if pos is not None:
        cant_ent_con_pokemon =+ 1

print()
print(f'Cantidad de entrenadores que tienen a Pikachu: {cant_ent_con_pokemon}')
print()

#i mostrar los entrenadores que tienen Pokémons repetidos;

for i in range(0, lista_entrenadores.size()):

    value= lista_entrenadores.get_element_by_index(i)

    entrenador, sublista = value[0], value[1]
   

    for pos in range(0, sublista.size()-1):
        actual = sublista.get_element_by_index(pos)
    
        siguiente = sublista.get_element_by_index(pos+1)

        if actual.nombre == siguiente.nombre:
            print(f"El entrenador {entrenador.nombre} tiene Pokemons repetidos.")
            break

print() 





#j

print("Los entrenadores que tienen los Pokemons Tyrantrum, Terrakion o Wingull son: ")

for i in range(0, lista_entrenadores.size()):

    value= lista_entrenadores.get_element_by_index(i)

    entrenador, sublista = value[0], value[1]

    pos=sublista.search('Terrakion', 'nombre')
    if pos is not None:
        print(entrenador)

    pos=sublista.search('Tyrantrum', 'nombre')
    if pos is not None:
        print(entrenador)

    pos=sublista.search('Wingull', 'nombre')
    if pos is not None:
        print(entrenador)

#k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

entrenador_ingresado= input('Ingrese el nombre del entrenador: ("Juan", "Jose" o "Maria"): ')
pokemon_ingresado= input('Ingrese el nombre del Pokemon: ("Pikachu", "Wingull", "Charmander", "Tyrantrum" o "Terrakion"): ')
encontrado= False

pos = lista_entrenadores.search(entrenador_ingresado, 'nombre')
value = lista_entrenadores.get_element_by_index(pos)

entrenador, sublista= value[0], value[1]

for i in range(0, sublista.size()):
    pokemon = sublista.get_element_by_index(i)

    if pokemon.nombre == pokemon_ingresado:
        encontrado= True
        print(f"El entrenador tiene al pokemon {pokemon_ingresado}")
        print("Datos: ")
        print(entrenador)
        print(pokemon)

        break

if encontrado == False:
    print(f"El entrenador no tiene al pokemon {pokemon_ingresado}")
