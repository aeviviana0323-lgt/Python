
suma = 0  # aquí guardaremos la suma de las notas

for i in range(4):
    nota = float(input(f"Ingrese la calificación {i + 1}: "))
    suma += nota  # se va sumando cada nota

promedio = suma / 4

print("El promedio de las calificaciones es:",promedio)