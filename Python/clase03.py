#%%
valor = 1000000
print(f"{valor:,}")

#%%
valor2 = 5.54353
print(f"{valor2:,.3f}")

precio = 10000
print(f"{"$" + str(precio):>15}")

#%%
numero1 = 5
numero2 = 24

print(numero2 /numero1)
print(numero1 / numero2)
# %%
numero1 = 9
numero2 = 3
print(numero1 % numero2)

# %%

# < menor 
# > mayor
# == comparacion 
# != distinto de
# <= menor o igual que
# >= mayor o igual que 

es_mayor = 5 > 100
print(es_mayor)

#%%
es_menor = 1000 < 500
print(es_menor)

# %%
numero1 = 1000
numero2 = 500
es_menor = numero1 < numero2
print(f"el numero {numero1} es menor a {numero2}? {es_menor}")
# %%
numero1 = 1000
numero2 = 500
es_mayor = numero1 > numero2
print(f"el numero {numero1} es mayor a {numero2}? {es_mayor}")

# %%
numero1 = 1000
numero2 = 500
es_distinto = numero1 != numero2
print(f"el numero {numero1} es distinto a {numero2}? {es_distinto}")
# %%
numero1 = 1000
numero2 = 500
es_igual = numero1 == numero2
print(f"el numero {numero1} es igual a {numero2}? {es_igual}")
# %%
numero1 = 1000
numero2 = 1000
es_igual = numero1 == numero2
print(f"el numero {numero1} es igual a {numero2}? {es_igual}")
# %%
# and
# or

cuenta_activa = False 
hay_internet = True
puedo_ver_peli = cuenta_activa and hay_internet

print(f"Puedo ver la peli? {puedo_ver_peli}")

# %%
total_compra = 200000
es_vip = True

hago_descuento = total_compra >= 50000 or es_vip 
print(f"Tiene descuento: {hago_descuento}")
# %%
suma = 4 + 5
suma += 1
print(suma)
# %%
texto = "   hola"
print(texto.strip())
# %%
texto = "hola"
print(texto.title())
# %%
texto = "HoLa"
print(texto.lower())
# %%
numero1 = 5
numero2 = 10

if numero1 < numero2:
    print(f"{numero1} es menor a {numero2}")
# %%

numero = 1

while numero <=10:
    print(numero)
    numero +=1 

#%%

nota1 = int(input("Ingrese nota1: "))
nota2 = int(input("Ingrese nota2: "))

promedio = (nota1 + nota2) / 2

aprobo = promedio >= 6


print(f"el promedio es: {promedio} , aprobo: {aprobo}")

# %%

