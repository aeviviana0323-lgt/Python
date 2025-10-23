A = float(input("Ingrese la altura total (A): "))
B = float(input("Ingrese la base (B): "))
C = float(input("Ingrese la altura del rectángulo (C): "))


area_triangulo = (B * (A - C)) / 2
area_rectangulo = B * C
area_total = area_triangulo + area_rectangulo


print("El área total del terreno es:",area_total)