def calcularPromedio(nota1, nota2):
    "Calcula el promedio de dos notas."
    promedio = (nota1 + nota2) / 2
    return promedio

if __name__ == "__main__":
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))

    resultado = calcularPromedio(nota1, nota2)
    print("El promedio es:", resultado)