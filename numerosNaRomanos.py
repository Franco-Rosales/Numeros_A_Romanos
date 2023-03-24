def numero_a_romano(numero):
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    resultado = ""
    i = 0
    while numero > 0:
        if numero - valores[i] >= 0:
            resultado += simbolos[i]
            numero -= valores[i]
        else:
            i += 1
    return resultado

numero = int(input("Introduce un número natural: "))
romano = numero_a_romano(numero)
print("El número romano equivalente es:", romano)
