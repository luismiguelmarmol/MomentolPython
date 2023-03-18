cuentas = []
codigoCuenta = 100
for i in range(3):
    diccionarioCuenta = {}
    codigoCuenta = codigoCuenta + 1
    diccionarioCuenta['codigo'] = codigoCuenta
    diccionarioCuenta['saldo'] = int(input(f'Ingrese el saldo de la cuenta #{codigoCuenta}: '))
    cuentas.append(diccionarioCuenta)

cuentas.sort(key=lambda cuenta: cuenta['saldo'])
cuentas.reverse()
print(cuentas)