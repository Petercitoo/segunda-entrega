def ingreso_datos():
    weight = int(input("Ingrese el peso del paquete en kgs: "))
    valido = False
    while not valido:
        dest = int(input("Elija el destino: \n 1.Local \n 2.Regional \n 3.Nacional "))
        if dest == 1:
            valido = True
        elif dest == 2:
            valido = True
        elif dest == 3:
            valido = True
        else:
            print("Destino invalido, elija nuevamente. Las zonas validas son" 
           "\n 1.Local \n 2.Regional \n 3.Nacional ")
    return weight, dest

def calculo_envio(weight,dest):
    if weight <= 1:
        if dest == 1:
            print("El coste de envio sera de 500$")
        elif dest == 2:
            print("El coste de envio sera de 1000$")
        else:
            print("El coste de envio sera de 2000$")
    elif 1<= weight <= 5:
        if dest == 1:
            print("El coste de envio sera de 1000$")
        elif dest == 2:
            print("El coste de envio sera de 2500$")
        else:
            print("El coste de envio sera de de 4500$")
    else:
        if dest == 1:
            print("El coste de envio sera de 2000$")
        elif dest == 2:
            print("El coste de envio sera de 5000$")
        else:
            print("El coste de envio sera de 8000$")

weight, dest = ingreso_datos()