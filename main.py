import random
import json

# BD User creation
def createUser():
    usersValues = []
    usersKeys = {}
    length = range(5)

    user = str(input('Ingrese su Nombre '))
    mail = str(input('ingrese su email '))
    rut = str(input('Ingrese su Rut '))
    clave = str(input('Ingrese su Clave '))
    deposito =str(50000)
    tarjeta = generarTarjeta()

    usersValues.append(user)
    usersValues.append(rut)
    usersValues.append(mail)
    usersValues.append(tarjeta)
    usersValues.append(clave)
    usersValues.append(deposito)

    for i in length: #Fill userKeys
        usersKeys[i] = usersValues[i]

    print(usersKeys)#DEBUGGING

    with open('./BD/ID'+tarjeta+'.json', 'w', encoding='utf-8') as convert_file: #Sending information as json
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
    print(numeroTarjeta)#DEBUGGING
    return numeroTarjeta

#BD User validation
def user():
    datos = []
    validaTarjeta = input("Ingrese Tarjeta ")
    
    with open('./BD/ID'+validaTarjeta+'.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)

    print(datos) #DEBUGGING
    print(datos['3'])#DEBUGGING
    print(datos['4'])#DEBUGGING
    intentos = 3

    while intentos != 0:
        if datos['3'] == validaTarjeta :
            print('La tarjeta es valida')#DEBUGGING
            validarClave = input("Ingrese Clave ")
   
            if datos['4'] == validarClave:
                print('Su clave es valida')#DEBUGGING   
                print('Usted tiene un saldo de: ' , datos['5'])
                retiro = input('cuanto desea retirar?')
                sacarDinero(datos,retiro,validaTarjeta)
            else:
                print('Clave erronea, ingrese su clave nuevamente')
                intentos -=1
            if intentos == 0:
                print('Su tarjeta sera bloqueada')

def sacarDinero(datos,retiro,tarjeta):
    dinero = []
    dineroCajero  = BDcajero()
    if dineroCajero > 0:
        dineroCliente = datos["5"]

        print('Usted ha retirado ' , retiro)

        if int(retiro) > 0:
            datos["5"] = int(dineroCliente) - int(retiro)
            print(datos)

        with open('./BD/ID'+tarjeta+'.json', 'w', encoding='utf-8') as convert_file:
            convert_file.write(json.dumps(datos))

    nuevoValor = int(dineroCajero) - int(retiro)
    dinero.append(nuevoValor)

    with open('./cajero.txt', 'w') as f: ##Voy aqui
        for d in dinero:
            f.write(str(d))
    
    exit()

#Saldo cajero
def BDcajero():
    saldo = []

    with open('./cajero.txt', 'r') as f:
        for line in f:
            saldo.append(line)

    saldoBase = ''.join(saldo)

    if int(saldoBase) > 1:
        print("El cajero tiene saldo de ", saldoBase)

    return int(saldoBase)

#Modifica saldo cajero
#    def dinero():
#       dinero = BDcajero()
#
#
#       return saldo


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