

palabras= ['hola', 'chau', 'hola', 'hola', 'dos', 'cuatro']

palabra= 'hola'



def contar_palabras(palabra, palabras, contador=0):
    if len(palabras) == 0:
        return contador
    
    if palabras[0]== palabra:
        return contar_palabras(palabra, palabras[1:], contador+1)
    
    else: 
        return contar_palabras(palabra, palabras[1:], contador)


print(contar_palabras(palabra, palabras))