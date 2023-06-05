from cola import Cola

personajes= [
{'nom_per': 'Tony Stark', 'nom_super': 'Iron Man', 'genero': 'M'},
{'nom_per': 'Steve Rogers', 'nom_super': 'Capitan America', 'genero': 'M'},
{'nom_per': 'Natasha Romanoff', 'nom_super': 'Black Widow', 'genero': 'F'},
{'nom_per': 'Carol Danvers', 'nom_super': 'Capitana Marvel', 'genero': 'F'},
{'nom_per': 'Scott Lang', 'nom_super': 'Ant Man', 'genero': 'M'},
{'nom_per': 'Peter Parker', 'nom_super': 'Spiderman', 'genero': 'M'}
]

cola = Cola()

for personaje in personajes:
    cola.arrive(personaje)


#a
def nom_cap_marvel():
    
    contador=0
    while contador < cola.size():
        
        value= cola.on_front()
        if value['nom_super'] == 'Capitana Marvel':
            return value['nom_per']
        else:
            cola.move_to_end()

        contador += 1 

print('a)')
print(nom_cap_marvel())
print()

#b
def nom_super_fem():
    
    nombres=[]

    contador =0
    while contador < cola.size():
        value= cola.on_front()

        if value['genero'] == 'F':
            nombres.append(value['nom_super'])
        
        cola.move_to_end()
        
        contador += 1
    
    return nombres

print('b)')     
for nombre in nom_super_fem():
    print(nombre)
print()


#c
def nom_super_masc():
    
    nombres=[]

    contador =0
    while contador < cola.size():
        value= cola.on_front()

        if value['genero'] == 'M':
            nombres.append(value['nom_super'])
        
        cola.move_to_end()
        
        contador += 1
    
    return nombres
        
print('c)')
for nombre in nom_super_masc():
    print(nombre)
print()

#d
def nom_scott():
    
    contador=0
    while contador < cola.size():
        
        value= cola.on_front()
        if value['nom_per'] == 'Scott Lang':
            return value['nom_super']
        else:
            cola.move_to_end()

        contador += 1 

print('d)')
print(nom_scott())
print()

#e

def nom_con_s():
    
    lista_datos=[]
    contador=0

    while contador < cola.size():
        value= cola.on_front()

        if value['nom_super'][0] == 'S' or value['nom_per'][0] =='S':
            lista_datos.append(value)
        
        cola.move_to_end()

        contador += 1
    return lista_datos


print('e)')
lista_datos=nom_con_s()

for datos in lista_datos:
    print(f"Nombre del personaje: {datos['nom_per']} - Nombre del superheroe: {datos['nom_super']} - Genero: {datos['genero']}")
   
print()


#f
def determinar_carol():
    '''determina si Carol Danvers se encuentra en la cola'''
    

    contador=0
    while contador < cola.size():
        
        value= cola.on_front()
        if value['nom_per'] == 'Carol Danvers':
            return True
        
        else:
            cola.move_to_end()

        contador += 1 
    return False

def nom_super_carol():
    '''devuelve el nombre de superheroe de carol danvers'''
    contador=0
    while contador < cola.size():
        
        value= cola.on_front()
        if value['nom_per'] == 'Carol Danvers':
            return value['nom_super']
        else:
            cola.move_to_end()

        contador += 1 


print('f)')
if determinar_carol() == True:   
    print(f"Carol Danvers se encuentra en la cola. Su nombre de superheroe es: {nom_super_carol()}")