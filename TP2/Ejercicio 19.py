from pila import Pila


peliculas= [{'title': 'iron man', 'year': 2014, 'studio': 'universal'},
            {'title': 'spiderman', 'year': 2018, 'studio': 'marvel'},
            {'title': 'avengers', 'year': 2016, 'studio': 'marvel'},
            {'title': 'deadpool', 'year': 2016, 'studio': 'marvel' }
]

peliculas_2014=[]
peliculas_marvel=[]
contador=0

pila_1= Pila()
for peli in peliculas:
    pila_1.push(peli)

while pila_1.size()>0:

    value=pila_1.pop()

    if value['year']== 2014:
        peliculas_2014.append(value['title'])
    
    if value['year']==2018:
        contador=contador+1
    
    if value['studio']=='marvel' and value['year']== 2016:
        peliculas_marvel.append(value['title'])


print('Peliculas estrenadas en 2014:')
for peli in peliculas_2014:
    print(peli)

print()
print(f'Peliculas estrenadas en 2018: {contador}')
print()

print('Peliculas de Marvel estrenadas en 2016:')
for peli in peliculas_marvel:
    print(peli)