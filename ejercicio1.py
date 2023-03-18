opcion = 1
ciclistas = []
codigo = 100
while opcion != 0:
    opcion = int(input('\nQue desea hacer?\n'
                    '\nOPCION #0: Salir\n'
                    'OPCION #1: Ingresar un ciclista\n'
                    'OPCION #2: Mostrar todas la tabla de posiciones\n'
                    'OPCION #3: Corrigir el tiempo del ciclista\n'
                    'OPCION #4: Eliminar ciclista\n'))
    if(opcion==1):
        ciclista = {}
        codigo = codigo + 1
        ciclista['codigo'] = codigo
        ciclista['nombre'] = input('Ingrese el nombre del ciclista: ')
        ciclista['edad'] = input('Ingrese la edad del ciclista: ')
        ciclista['pais'] = input('Ingrese el pais del ciclista: ')
        ciclista['equipo'] = input('Ingrese el equipo del ciclista: ')
        ciclista['tiempo'] = int(input('Ingrese el tiempo del ciclista: '))
        ciclistas.append(ciclista)
        print('Ciclista Registrado')
    elif(opcion==2):
        for ciclista in ciclistas:
            print(ciclista)
    elif(opcion==3):
        buscarCiclista = int(input('Digite el codigo del ciclista a buscar: '))
        for ciclista in ciclistas:
            if(ciclista['codigo'] == buscarCiclista):
                print(f'El tiempo actual del ciclista es: {ciclista["tiempo"]}')
                ciclista['tiempo'] = int(input('Digite el nuevo tiempo: '))
    elif(opcion==4):
        buscarCiclista = int(input('Digite el codigo de la ciclista a eliminar: '))
        for ciclista in ciclistas:
            if(ciclista['codigo'] == buscarCiclista):
                ciclistas.remove(ciclista)
                print('Ciclista Eliminado Correctamente')
            else:
                print('Ciclista no existe')