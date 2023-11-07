from arbol_binario import BinaryTree

arbol_nombre = BinaryTree()

arbol_numero = BinaryTree()

arbol_tipo = BinaryTree()


pokemons = [
    {'nombre': 'Pikachu', 'tipo': 'Electrico', 'numero': 25},
    {'nombre': 'Bulbasaur', 'tipo': 'Planta', 'numero': 1},
    {'nombre': 'Charizard', 'tipo': 'Fuego', 'numero': 6},
    {'nombre': 'Squirtle', 'tipo': 'Agua', 'numero': 7},
    {'nombre': 'Tyrantrum', 'tipo': 'Planta', 'numero': 3},
    {'nombre': 'Raichu', 'tipo': 'Electrico', 'numero': 26},
    {'nombre': 'Blastoise', 'tipo': 'Agua', 'numero': 9},
    {'nombre': 'Charmander', 'tipo': 'Acero', 'numero': 4},
    {'nombre': 'Lycanroc', 'tipo': 'Agua', 'numero': 130},
    {'nombre': 'Jolteon', 'tipo': 'Electrico', 'numero': 133},
]




for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], pokemon)
    arbol_tipo.insert_node(pokemon['tipo'], pokemon)
    arbol_numero.insert_node(pokemon['numero'], pokemon)


# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;

numero = 1

pokemon = arbol_numero.search(numero)

print(f"{pokemon.value} - {pokemon.other_values['nombre']} - {pokemon.other_values['tipo']} ")

print()
arbol_nombre.search_by_coincidence('B')


#mostrar todos los nombres de todos los Pokémons de un determinado tipo 

print("tipo agua")
arbol_nombre.inorden_pokemon_tipo('Agua')
print()
print("tipo fuego")
arbol_nombre.inorden_pokemon_tipo('Fuego')
print()
print("tipo electrico")
arbol_nombre.inorden_pokemon_tipo('Electrico')
print()
print("tipo planta")
arbol_nombre.inorden_pokemon_tipo('Planta')
print()

# realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;

print("listado por nombre ascendente")
arbol_nombre.postorden_pokemon_nombre()
print()
print("listado por numero ascendente")
arbol_numero.postorden_pokemon_numero()
print()
print("listado por nivel (nombre)")
arbol_nombre.by_level()
print()


#mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;

print('Datos Jolteon')
nombre = 'Jolteon'

pokemon = arbol_nombre.search(nombre)

print(f"{pokemon.value} - {pokemon.other_values['numero']} - {pokemon.other_values['tipo']} ")
print()
print('Datos Lycanroc')
nombre = 'Lycanroc'

pokemon = arbol_nombre.search(nombre)

print(f"{pokemon.value} - {pokemon.other_values['numero']} - {pokemon.other_values['tipo']} ")
print()
print('Datos Tyrantrum')

nombre = 'Tyrantrum'

pokemon = arbol_nombre.search(nombre)

print(f"{pokemon.value} - {pokemon.other_values['numero']} - {pokemon.other_values['tipo']} ")
print()

#determinar cuantos pokemons de eletrico y acero hay

contador = arbol_tipo.contar_heroes_acero_fuego()

print("cantidad de pokemons de acero y fuego")
print(contador)