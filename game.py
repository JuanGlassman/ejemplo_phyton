from random import choice, randrange
from datetime import datetime
# Operadores posibles.
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver.
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
correctos = 0
for i in range(0, times):
    # Se eligen números y operador al azar.
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado.
    result = int(input("resultado: "))

    #Se repite el siguiente procedimiento con cada operador.
    if (operator == "+"): # Se verifica si es el operador correcto.
        if (number_1 + number_2 == result): # Se realiza la operación y se compara con el resultado.
            print("Resultado Correcto") 
            correctos += 1
        else:
            print("Resultado Incorrecto")
    elif (operator == "-"):
        if (number_1 - number_2 == result):
            print("Resultado Correcto")
            correctos += 1
        else:
            print("Resultado Incorrecto")
    elif (operator == "*"):
        if (number_1 * number_2 == result):
            print("Resultado Correcto")
            correctos += 1
        else:
            print("Resultado Incorrecto")
    elif (operator == "/"):
        if ((number_1 != 0) and (number_2 != 0)): # Se verifica que la division no sea por 0 asi no genera error.
            if (number_1 / number_2 == result):
                print("Resultado Correcto")
                correctos += 1
            else:
                print("Resultado Incorrecto")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
# Mostramos cuantas respuestas correctas e incorrectas tiene.
print (f"Tenes {correctos} respuestas correctas y {times - correctos} respuestas incorrectas")
