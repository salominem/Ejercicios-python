#%%
texto = "hOLA"

texto_cap = texto.capitalize()

print(texto_cap)
# %%

email = "sebasalomon@GMAIL.COM"
print(email.lower())
# %%

codigo = "descuento50"
es_valido = codigo.upper() == "DESCUENTO50"
print(f"tenes un descuento: {es_valido}")

# %%
usuario = input("Ingrese su usuario: ")
usuario_limpio = usuario.strip()

print(f"Antes tenia {len(usuario)} caracteres")
print(f"Antes tenia {len(usuario_limpio)} caracteres")
# %%
nombre = input("Ingresa un nombre: ")
print(nombre.title())
# %%
nombre = "  sEBA  "
print(nombre.strip().capitalize())
# %%
nombre = "jose".replace("e" , "é")
print(nombre)
# %%
codigo = "US-9875"
codigo_pais = codigo[0:2]
print(f"el codigo del pais es: {codigo_pais}")
# %%
nro_tarjeta = "2345235235235123"
ultimos_digitos = nro_tarjeta[0:5]
print(f"Los primeros 5 digitos son: {ultimos_digitos}")
# %%
registro = "2026-07-19"
print(registro[:4])
# %%
registro = "2026-07-19"
print(registro[-4:])

# %%
registro = "2026-07-19"
print(registro[:6])
# %%

palabra = "123456789"

palabra_invertida = palabra[::-1]

print(palabra_invertida)

es_palindromo = palabra == palabra_invertida

print(f"La palabra es palindromo: {es_palindromo}")

# %%
texto = "0123456789"
print(texto[2:6])
# %%

archivo = "clase_python4.pdf"

extension = archivo[-4:]
print(f"La extension del archivo es: {extension}")
# %%

grado = float(input("Ingrese el grado: "))

f = (grado * 1.8) + 32

print(f"el resultado de grado Celcius {grado} convertido a Fahrenheit es: {f} ")
# %%

lista = [1,2,3,"A","B",True]

print(lista[2])

ultimo_elemento = lista.pop()
print(ultimo_elemento)

lista.remove("A")
print(lista)

lista.clear()
print(lista)

# %%
lista = [1,2,3,"A","B",True]

valor = "B"

if valor in lista:
    print(f"{valor} si está")
    
lista[0] = "Hola"
print(lista)
