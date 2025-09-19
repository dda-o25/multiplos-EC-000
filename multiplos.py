"""
Multiplos
El propósito de este programa es calcular si un numero dado es multiplo de otro numero, y en caso contrario madnar un mensaje de error
Eduardo Caleb Castillo Llanas 18/Sep/25
"""

valor_1 = int(input("Primer número: "))
valor_2 = int(input("Segundo número: "))
prueba_1 = valor_2 % valor_1
prueba_2 = valor_1 % valor_2

# Proces0
if prueba_1 == 0:
    print(valor_2, "es múltiplo de", valor_1)
elif prueba_2 == 0:
    print(valor_1, "es múltiplo de", valor_2)
else:
    print("Ninguno de los números es múltiplo del otro")
