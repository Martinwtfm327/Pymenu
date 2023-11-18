import math

#Ejercicio a realizar despues de seleccionar una opcion
def suma_numeros():
    n = int(input("Ingrese la cantidad de números a sumar: "))
    suma = 0
    for _ in range(n):
        suma += float(input("Ingrese un número: "))
    print(f"La suma de los números es: {suma}")

def producto_numeros():
    n = int(input("Ingrese la cantidad de números a multiplicar: "))
    producto = 1
    for _ in range(n):
        producto *= float(input("Ingrese un número: "))
    print(f"El producto de los números es: {producto}")

def division_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división de {num1} entre {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")

def factorial_numero():
    n = int(input("Ingrese un número para calcular su factorial: "))
    resultado = math.factorial(n)
    print(f"El factorial de {n} es: {resultado}")

def tablas_multiplicar():
    num_tabla = int(input("Ingrese el número para mostrar su tabla de multiplicar: "))
    for i in range(1, 11):
        print(f"{num_tabla} x {i} = {num_tabla * i}")

def cuadrado_y_cubo():
    num = float(input("Ingrese un número para calcular su cuadrado y cubo: "))
    cuadrado = num ** 2
    cubo = num ** 3
    print(f"El cuadrado de {num} es: {cuadrado}")
    print(f"El cubo de {num} es: {cubo}")

def promedio_numeros():
    valores = []
    while True:
        valor = float(input("Ingrese un número (-1 para terminar): "))
        if valor == -1:
            break
        valores.append(valor)
    if valores:
        promedio = sum(valores) / len(valores)
        print(f"El promedio de los números es: {promedio}")
    else:
        print("No se ingresaron valores.")

def maximo_y_minimo():
    n = int(input("Ingrese la cantidad de números a comparar: "))
    if n > 0:
        valores = [int(input("Ingrese un número: ")) for _ in range(n)]
        maximo = max(valores)
        minimo = min(valores)
        print(f"El valor máximo es: {maximo}")
        print(f"El valor mínimo es: {minimo}")
        print(f"Total de valores ingresados: {n}")
    else:
        print("La cantidad de números debe ser mayor que cero.")

# Menú principal al ejecutar el programa
while True:
    print("\nMenú de opciones:")
    print("1. Suma de x números")
    print("2. Producto entre n números")
    print("4. Factorial de un número")
    print("5. Tablas de multiplicar")
    print("6. Cuadrado y cubo de un número")
    print("7. Promedio de una serie de números")
    print("8. Valor máximo y mínimo")
    print("9. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        suma_numeros()
    elif opcion == "2":
        producto_numeros()
    elif opcion == "3":
        division_numeros()
    elif opcion == "4":
        factorial_numero()
    elif opcion == "5":
        tablas_multiplicar()
    elif opcion == "6":
        cuadrado_y_cubo()
    elif opcion == "7":
        promedio_numeros()
    elif opcion == "8":
        maximo_y_minimo()
    elif opcion == "9":
        print("¡Hasta luego, vuelva pronto!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 9.")
