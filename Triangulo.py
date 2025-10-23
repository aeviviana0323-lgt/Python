
H = float(input("Ingrese la hipotenusa (H): "))
R = float(input("Ingrese el cateto o radio (R): "))

h = (H*2 - R*2) ** 0.5     
Area = (R * h) + (3.1416 * R**2 / 2)


print("La altura del triángulo es:", h)
print("El área total de la figura es:",Area)