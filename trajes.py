precio = float(input("Ingrese el precio del traje: "))

descuento = precio * (0.15 if precio > 2500 else 0.08)

precio_final = precio - descuento

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")