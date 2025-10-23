

personas = int(input("Ingrese el número de personas: "))


costo = 95 if personas <= 200 else 85 if personas <= 300 else 75


presupuesto = personas * costo


print("Costo por persona:", costo)
print("Presupuesto total:",presupuesto)