#Parte 1
print("Semana No. 12: Ejercicio 1")
def ObtenerAreaTriangulo(base, altura):
    return (base * altura) / 2

def ObtenerAreaCuadrado(lado):
    return lado ** 2

def ObtenerAreaRectángulo(base, altura):
    return base * altura

def ObtenerAreaCírculo(radio):
    return 3.14159 * (radio ** 2)

def main():
    while True:
        print("\nOpciones:")
        print("a. Área de triángulo")
        print("b. Área de cuadrado")
        print("c. Área de rectángulo")
        print("d. Área de círculo")
        print("e. Salir")

        opcion = input("¿Qué opción deseas? (a, b, c, d, e): ")

        if opcion == "a":
            base = int(input("Introduce la base del triángulo: "))
            altura = int(input("Introduce la altura del triángulo: "))
            print(f"El área del triángulo es: {ObtenerAreaTriangulo(base, altura)}")
        elif opcion == "b":
            lado = int(input("Introduce el lado del cuadrado: "))
            print(f"El área del cuadrado es: {ObtenerAreaCuadrado(lado)}")
        elif opcion == "c":
            base = int(input("Introduce la base del rectángulo: "))
            altura = int(input("Introduce la altura del rectángulo: "))
            print(f"El área del rectángulo es: {ObtenerAreaRectángulo(base, altura)}")
        elif opcion == "d":
            radio = int(input("Introduce el radio del círculo: "))
            print(f"El área del círculo es: {ObtenerAreaCírculo(radio)}")
        elif opcion == "e":
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

#Parte 2    
x = 0
y = 0

def MoverPosicion(cantX, cantY):
    global x, y
    x += cantX
    y += cantY


opcion = 'a'
while(opcion !='e'):
    print("Menu")
    print("a.Sube","b.Baja","c.Izquierda","d.Derecha","e.Salir", sep ="\t\n")  
    opcion = input("ingrese su opcion:")

    match opcion:
        case 'a':
            MoverPosicion(0,1)
        case 'b':
            MoverPosicion(0,-1)
        case 'c':
            MoverPosicion(-1,0)
        case 'd':
            MoverPosicion(1,0)
        case _:
            print("Error: debe ingresar una letra a-e")

    print(f"La posicion actal es :[{x}],[{y}]")

