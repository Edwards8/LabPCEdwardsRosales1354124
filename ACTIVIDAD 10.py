# Definición de los menús de desayuno, almuerzo y cena
menu_desayuno = {
    "Huevos con tocino": 5.99,
    "Panqueques con miel": 6.49,
    "Tostadas francesas": 4.99
}

menu_almuerzo = {
    "Hamburguesa con papas fritas": 8.99,
    "Ensalada César": 7.49,
    "Sándwich de pollo": 6.99
}

menu_cena = {
    "Pizza de pepperoni": 10.99,
    "Pasta Alfredo": 9.49,
    "Salmón a la parrilla": 12.99
}

# Función para mostrar el menú y obtener la selección del usuario
def seleccionar_plato(menu):
    print("Menú:")
    for plato, precio in menu.items():
        print(f"{plato}: ${precio}")
    seleccion = input("Seleccione un plato: ")
    return seleccion

# Función para calcular el valor total de la orden
def calcular_total(orden, menu):
    total = 0
    for plato in orden:
        if plato in menu:
            total += menu[plato]
    return total

# Función principal
def main():
    orden_desayuno = []
    orden_almuerzo = []
    orden_cena = []

    while True:
        print("\n1. Desayuno")
        print("2. Almuerzo")
        print("3. Cena")
        print("4. Pagar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            plato_desayuno = seleccionar_plato(menu_desayuno)
            orden_desayuno.append(plato_desayuno)
        elif opcion == "2":
            plato_almuerzo = seleccionar_plato(menu_almuerzo)
            orden_almuerzo.append(plato_almuerzo)
        elif opcion == "3":
            plato_cena = seleccionar_plato(menu_cena)
            orden_cena.append(plato_cena)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    total_desayuno = calcular_total(orden_desayuno, menu_desayuno)
    total_almuerzo = calcular_total(orden_almuerzo, menu_almuerzo)
    total_cena = calcular_total(orden_cena, menu_cena)

    total_pagar = total_desayuno + total_almuerzo + total_cena
    print(f"\nTotal a pagar: ${total_pagar:.2f}")

# Llamada a la función principal
if __name__ == "__main__":
    main()