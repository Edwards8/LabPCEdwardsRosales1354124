print("semana no.11: Ejercicio 1")
n = int(input("Ingrese un numero mayor a cero"))

if(n <= 0):
    print("Error, debe ser mayor a cero")
          
#Definicion de Varibales para fibonacci
a=0
b=1
c=0

i=2
resultado=""

if (n>0):
    resultado = str(a)

    if(n>1):
        resultado = resultado + "," + str(b)    

        #Ciclo, se repite hasta que se deje de cumplir la condicion
        while (i < n):
                c = a + b 
                resultado = resultado + "," + str(c)    
                a = b
                b = c
                i = i + 1
    print(resultado)
else:
    print(resultado)

print("Semana No.11: Ejercicio No.02")
n2 = int(input("Ingrese un numero mayor a cero"))

if(n2 <= 0):
    print("Error, debe ser mayor a cero")
#Ejercicio A
CalculoA = 0
for xA in range(1, n2 + 1):
     CalculoA += 1 / xA
print("El resultado de A es:", CalculoA)
#Ejercicio B
CalculoB = 0
for xB in range(1, n2 + 1):
     CalculoB += 1 / (2 ** xB)
print("El resultado de B es:", CalculoB)
