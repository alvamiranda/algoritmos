from cola import Cola
from pila import Pila

pila = Pila()
cola = Cola()


notificaciones= [
    {'hora': 12, 'app': 'Facebook', 'mensaje': 'Nueva solicitud de amistad'},
    {'hora': 6, 'app': 'Twitter', 'mensaje': 'Python'},
    {'hora': 4, 'app': 'Facebook', 'mensaje': 'Nueva solicitud de amistad'},
    {'hora': 1, 'app': 'Twitter', 'mensaje': 'Python'},
    {'hora': 9, 'app': 'Facebook', 'mensaje': 'Nueva solicitud de amistad'}
]


for notificacion in notificaciones:
    cola.arrive(notificacion)

#Eliminar notificaciones de facebook
def elim_notif_fb():

    contador=0
    tamanio=cola.size()
    while contador < tamanio:
        value= cola.on_front()

        if value['app'] == 'Facebook':
            cola.attention()
        else:
            cola.move_to_end()
            contador += 1
        
#Mostrar notificaciones de Twitter con  el mensaje 'Python'
def mensaje_python():
    contador=0

    while contador < cola.size():
        value= cola.on_front()

        if value['mensaje'] == 'Python' and value['app'] == 'Twitter':
            return print(f"Hora {value['hora']} - App: {value['app']} - Mensaje: {value['mensaje']}" )
        
        cola.move_to_end()
        contador += 1
    
mensaje_python()

# pila para almacenar temporáneamente las notificaciones producidas entre las 
# 11:43 y las 15:57, y determinar cuántas son.


contador=0
while contador < cola.size():

    value= cola.on_front()
    if value['hora'] > 11.47 and value['hora'] < 15.57:
        pila.push(value)



    cola.move_to_end()

    contador += 1

print()
print(f'Cantidad de notificaciones entre las 11.43 y las 15.57:  {pila.size()}')