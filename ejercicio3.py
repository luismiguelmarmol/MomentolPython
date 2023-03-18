import random

tamano = 20
numeros = [random.randint (0, 20) for i in range(tamano)]
multiplosDos = 0
multiplosTres = 0
multiplosSimultaneo = 0
for numero in numeros:
    if numero % 2 == 0 and numero % 3 == 0:
        multiplosSimultaneo = multiplosSimultaneo + 1
    elif numero % 3 == 0:
        multiplosTres = multiplosTres + 1
    elif numero % 2 == 0:
        multiplosDos = multiplosDos + 1
print(numeros)
print(f'La cantidad de numeros multiplos de 2 son: {multiplosDos}')
print(f'La cantidad de numeros multiplos de 3 son: {multiplosTres}')
print(f'La cantidad de numeros multiplos simultaneos son: {multiplosSimultaneo}')
        



