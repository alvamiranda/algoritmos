
numero='XXII'

def convertir_rom_a_dec(letra):
    valor_romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(letra)==1:
         return valor_romano[letra[0]]
    else:
          if valor_romano[letra[0]] >= valor_romano[letra[1]]:
               return valor_romano[letra[0]] + convertir_rom_a_dec(letra[1:])
        
          else:
               return - valor_romano[letra[0]] + convertir_rom_a_dec(letra[1:])
              

    

print(convertir_rom_a_dec(numero))

    

    
    
