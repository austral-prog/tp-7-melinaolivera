   def enumerate_list(strings):
    result = []
    for index, value in enumerate(strings):
        if value:  # Si el valor no es una cadena vacía
            result.append(f"{index}. {value}")
    return result

# Ejemplo de uso
colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_list(colors))  # ["0. Red", "1. Green", "3. White", "4. Black"]

def enumerate_backwards(strings):
    result = []
    for index, value in enumerate(strings):
        if value:  # Si el valor no es una cadena vacía
            result.append(f"{index}. {value[::-1]}")
    return result

# Ejemplo de uso
colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_backwards(colors))  # ["0. deR", "1. neerG", "3. etihW", "4. kcalB"]
