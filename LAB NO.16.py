import random

print("Semana No.16: Ejercico 1")

lista = [list]

for i in range(1,11):
    lista.append(random.randint(0,10))

opcion = 'a'

while(opcion!='e'):
    print("Menu")
    print("a.Mostrar numeros","b.Promedio","c.Longitud","d.Posicion", sep ="\t\n")
    opcion = input("Ingrese su opcion: ")

    match opcion:
        case'a':#Opcion mostrar numeros
            for i in range(len(lista)):
                print(f"No. {i}:{lista[i]}")

        case 'b':#Opcion promedio
            sumatoria = 0
            for i in range(len(lista)):
                sumatoria += str (lista[i])
            promedio = sumatoria / len(lista)
            print(f"-----Promedio: {promedio}")

        case'c' :# Mostrar longitud
            print(f"----- Longitud de la lista: {len(lista)}")
        
        case'd' : #Opcion Posiciones Pares e Impares
            suma_pares = sum(lista[i] for i in range(len(lista)) if i % 2 == 0)
            suma_impares = sum(lista[i] for i in range(len(lista)) if i % 2 != 0)
            print(f"----- Suma de posiciones pares: {suma_pares}")
            print(f"----- Suma de posiciones impares: {suma_impares}")


#Actividad 2

print("Semana No.12": Ejercicio 2)

cantFilas = int(input("Ingrese la cantidad de filas"))
cantCols= int(input("Ingrese la cantidad de columnas"))

matriz = [[0 for x in range(cantCols)]for y in range(cantFilas)]

for xFilas in range(cantFilas):
    for xCols in range(cantCols):
        matriz[xFilas][xCols] = random.randit(0,1000)
       
        if(matriz[xFilas][xCols] > mayor):  
            mayor = matriz[xFilas][xCols]
            pares = sum(1 for fila in matriz for num in fila if num % 2 == 0)
            impares = sum(1 for fila in matriz for num in fila if num % 2 != 0)
            menor = min(min(fila) for fila in matriz)
print(matriz)
print(f"\nCantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")



