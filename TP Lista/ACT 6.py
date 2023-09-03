from lista_lista import Lista

class Superheroe():
    
    def __init__(self, nombre, anio_ap, casa_com, biografia):
        self.nombre= nombre
        self.anio_ap= anio_ap
        self.casa_com= casa_com
        self.biografia = biografia

    def __str__(self):
        return f"{self.nombre} - {self.anio_ap} - {self.casa_com} - {self.biografia}"
    
sup1= Superheroe("Linterna Verde", 1940, "DC", "Linterna Verde es un título compartido por varios personajes, cada uno de los cuales es miembro de la Fuerza de Linterna Verde, que protege el universo utilizando anillos que crean construcciones de energía pura")
sup2= Superheroe("Wolverine", 1974, "Marvel", "traje")
sup3= Superheroe("Doctor Strange", 1963, "DC", "El Doctor Stephen Strange es un cirujano convertido en hechicero maestro tras un accidente automovilístico. Protege la realidad de amenazas místicas utilizando su magia y conocimiento.")
sup4= Superheroe("Capitana Marvel", 1967, "Marvel", "Carol Danvers, también conocida como Capitana Marvel, obtiene poderes cósmicos tras un accidente con una tecnología alienígena. Es una poderosa heroína que lucha en el espacio y la Tierra.")
sup5= Superheroe("Mujer Maravilla", 1941, "DC", "armadura")
sup6= Superheroe("Flash", 1940, "DC", "Barry Allen es un científico que obtiene habilidades de super velocidad después de ser alcanzado por un rayo. Se convierte en The Flash, el defensor de Ciudad Central.")
sup7= Superheroe("Star-Lord", 1976, "Marvel", "Peter Quill, conocido como Star-Lord, es un aventurero espacial y líder de los Guardianes de la Galaxia. Posee habilidades de combate y un profundo amor por la música.")

superheroes= [sup1, sup2, sup3, sup4, sup5, sup6, sup7]

lista_superheroes = Lista()

for superheroe in superheroes:
    lista_superheroes.insert(superheroe, 'nombre')


#a
lista_superheroes.delete('Linterna Verde', 'nombre')

print()
lista_superheroes.barrido_superheroes()
print()

#b mostrar el año de aparición de Wolverine

pos = lista_superheroes.search('Wolverine', 'nombre')

value = lista_superheroes.get_element_by_index(pos)[0]

print(f"Año de aparicion de Wolverine: {value.anio_ap}")
print()

#c cambiar la casa de Dr. Strange a Marvel

pos = lista_superheroes.search('Doctor Strange', 'nombre')

value = lista_superheroes.get_element_by_index(pos)[0]

value.casa_com = 'Marvel'
print()

#d mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;


print("superhéroes que en su biografía menciona la palabra traje o armadura: ")
for i in range(0, lista_superheroes.size()):

    value = lista_superheroes.get_element_by_index(i)[0]

    if ((value.biografia.find('armadura') != -1) or (value.biografia.find('traje') != -1)):
        print(value.nombre)

print()
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;

print("superhéroes cuya fecha de aparició es anterior a 1963:")
lista_superheroes.barrido_1963()

print()

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;

pos = lista_superheroes.search('Capitana Marvel', 'nombre')

value = lista_superheroes.get_element_by_index(pos)[0]

print(f"La casa a la que pertenece Capitana Marvel es {value.casa_com}")

pos = lista_superheroes.search('Mujer Maravilla', 'nombre')

value = lista_superheroes.get_element_by_index(pos)[0]

print(f"La casa a la que pertenece Mujer Maravilla es {value.casa_com}")

print()

# g. mostrar toda la información de Flash y Star-Lord;

lista_superheroes.info_superheroe('Flash', 'nombre')
lista_superheroes.info_superheroe('Star-Lord', 'nombre')

print()
# h. listar los superhéroes que comienzan con la letra B, M y S;

print("superhéroes que comienzan con la letra B, M y S: ")

for i in range(0, lista_superheroes.size()):
    value= lista_superheroes.get_element_by_index(i)[0]
    if (value.nombre[0] == 'B') or (value.nombre[0] == 'M') or (value.nombre[0] == 'S'):
        print(value)

print()
# i. determinar cuántos superhéroes hay de cada casa de comic

contador_marvel= 0
contador_dc= 0

for i in range(0, lista_superheroes.size()):
    value= lista_superheroes.get_element_by_index(i)[0]

    if value.casa_com == 'Marvel':
        contador_marvel += 1


    if value.casa_com == 'DC':
        contador_dc += 1


print(f"Cantidad de superheroes en Marvel: {contador_marvel}")
print(f"Cantidad de superheroes en DC: {contador_dc}")
