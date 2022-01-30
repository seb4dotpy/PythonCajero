import random
import json
from typing import ClassVar

# BD User creation
def createUser():
    usersValues = []
    usersKeys = {}
    length = range(5)

    user = str(input('Ingrese su Nombre'))
    mail = str(input('ingrese su email'))
    rut = str(input('Ingrese su Rut'))
    clave = str(input('Ingrese su Clave'))
    tarjeta = generarTarjeta()

    usersValues.append(user)
    usersValues.append(rut)
    usersValues.append(mail)
    usersValues.append(tarjeta)
    usersValues.append(clave)

    for i in length: #Fill userKeys
        usersKeys[i] = usersValues[i]

    print(usersKeys)

    with open('./BD/ID'+tarjeta+'.txt', 'w', encoding='utf-8') as convert_file: #Sending information as json
        convert_file.write(json.dumps(usersKeys))

#BD Card generator
def generarTarjeta():
    numerosParaCodigo = ['1','2','3','4','5','6','7','8','9','0']
    letrasParaCodigo = ['a','e','i','o','u']
    numeros = numerosParaCodigo + letrasParaCodigo
    tarjeta = []

    for i in range(16):
        numeroRandom = random.choice(numeros)
        tarjeta.append(numeroRandom)
    
    numeroTarjeta = ''.join(tarjeta)
    print(numeroTarjeta)
    return numeroTarjeta

#BD User validation
def user():
    pass

#Saldo cajero
def BDcajero():
    saldo = []

    with open('./cajero.txt', 'r') as f:
        for line in f:
            saldo.append(line)

    saldodisponible = ''.join(saldo)

    if int(saldodisponible) > 1:
        print("El cajero tiene saldo de ", saldodisponible)
    return saldodisponible

#Menu
def options(choice): #Menu Choice validation
    if choice == 1:
        createUser()
        menu()
    elif choice == 2 :
        BDcajero()
        user()
        menu()
    elif choice == 3 :
        print('Adios')
    else:
        print('Por favor elija una alternativa valida')
        menu()

def menu(): #Main menu
    print('''
        #########################
        #     Bienvenida(o)     #
        #########################
        # 1.- Crear usuario     #
        # 2.- Usuario existente # 
        # 3.- Salir             #
        #########################   
    ''')
def main(): #Main option menu selection
    menu()
    choice = 1
    while choice != 3:
        choice = int(input('Ingrese una opcion: '))
        options(choice)
##
    



if __name__ == '__main__':
    main()