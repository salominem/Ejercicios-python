# %%

saldo = 100000

retiro = int(input("Ingrese su retiro: "))

if retiro > saldo:
    print("Saldo insuficiente")
elif retiro == saldo:
    print("Retiro exitoso!")
else:
    saldo -= retiro
    print(f"Tu saldo es {saldo:,.2f}")
# %%

usuario = "maxi"
clave = 123
pregunta = input("Ingrese su usuario: ")
clavemadre = int(input("Ingrese su clave"))

if usuario == pregunta and clavemadre == clave:
    print(f"Bienvenido {usuario}!")
elif usuario != pregunta:
    print("Usuario incorrecto.")
elif clavemadre != clave:
    print("Contraseña incorrecta.")
    
    
# %%

total_compra = 4000
tiene_cupon = True

if total_compra > 5000:
    print("Tiene descuento!")
elif total_compra < 5000:
    print("No tiene descuento") 
# %%

productos = ["teclado","monitor","mouse","auricular"]

productos.append("parlante")

print(productos)


# %%

productos = ["teclado","monitor","mouse","auricular"]

print(productos)

productos[1] = "CPU"

print(productos)

# %%

usuario = ["jesus","123","28",True]
usuario.append("gatos")
# usuario.pop()
# del usuario[0]
# usuario.remove("123")
print("Total de datos: ")
print(len(usuario))
print(usuario)
# print(usuario[0],usuario[1],usuario[3])

# %%

nombre = input("Ingrese un nombre: ")

nombre_limpio = nombre.strip().upper()

print(nombre_limpio)

# %%

print("Calificador de Notas")

nota = int(input("Ingrese su nota: "))
if nota < 0 or nota > 100:
    print("Error. Nota invalida")
elif nota >= 90 :
    print("Exelente!, tienes una A")
elif nota >= 70:
    print("Aprobado!, buen trabajo!")
else:
    print("Reprobado, necesitas estudiar mas.")
print("Fin.")


# %%

print("\n----- Resumen del Día -----")

inicio = float(input("Ingrese inicio de caja: "))
total_venta = float(input("Ingrese el total de ventas: "))
total_gastos = float(input("Ingrese el total de gastos: "))
ingreso_neto = total_venta - total_gastos
porcentaje_ganancia = ingreso_neto * 0.3 
caja_final = inicio + porcentaje_ganancia

print(f"Inicio de caja: ${inicio:,.2f}")
print(f"El total de ingresos del dia es: ${total_venta:,.2f}")
print(f"El total de gastos del dia es: ${total_gastos:,.2f}")
print(f"El total de ganancia neta del dia es: ${ingreso_neto:,.2f}")
print(f"El porcentaje de ganancia obtenida es: ${porcentaje_ganancia:,.2f}")
print(f"Caja final: ${caja_final:,.2f}")


print("Fin del dia.")



# %%

nota = int(input("Ingrese su nota: "))

if nota < 0 or nota > 100:
    print("Nota invalida.")
elif nota >= 90: 
    print("¡Excelente! Tienes una A")
elif nota >= 70:
    print("Aprobado.Buen trabajo")
else:
    print("Reprobado.")

