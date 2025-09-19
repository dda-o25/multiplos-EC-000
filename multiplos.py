"""
Multiplos
El propósito de este programa es calcular si un numero dado es multiplo de otro numero, y en caso contrario madnar un mensaje de error
Eduardo Caleb Castillo Llanas 18/Sep/25
"""

valor_1 = int(input())
valor_2 = int(input())

# Primero validamos ceros
if valor_1 == 0 or valor_2 == 0:
    print("No se puede verificar múltiplos con 0")
else:
    if valor_2 % valor_1 == 0:
        print("El número", valor_2, "es múltiplo del", valor_1)
    elif valor_1 % valor_2 == 0:
        print("El número", valor_1, "es múltiplo del", valor_2)
    else:
        print("Ninguno de los números es múltiplo del otro")
