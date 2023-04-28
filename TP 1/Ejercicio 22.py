mochila=[ 'a','b', 'c', 'sable', 'h', 'y']
cont=0


def usar_la_fuerza(mochila, cont):
    if len(mochila)==0:
        return f"Sable no encontrado, se quitaron {cont} objetos"
    elif mochila[0]=='sable':
        return f"Sable encontrado, se quitaron {cont} objetos"
    else:
        mochila.pop(0)
        cont = cont+1
        return usar_la_fuerza(mochila, cont)
    

print(usar_la_fuerza(mochila,cont)) 