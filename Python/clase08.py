#%%
stock_productos = ["Cafe", "Medialuna", "Tostado", "Jugo"]
producto_buscado = "Tostado"

encontro = False
indice = 0

while not encontro and indice < len(stock_productos):
    encontro = stock_productos[indice] == producto_buscado
    
    if encontro:
        print("Producto encontrado.")
        indice += 1

if not encontro:
    print("El producto no fue encontrado.")

#%%
transacciones = [10, -50, 30, -40, 15]
total_positivo = 0
for monto in transacciones:
    if monto <= 0:
        continue
    total_positivo += monto
    print(monto)
print(total_positivo)

cliente = ["Ana","ana@email.com",28,"Buenos Aires"]

print(cliente[2])

#%%
cliente = {
    "nombre" : "Ana",
    "mail" : "ana@gmail.com",
    "edad" : 28, 
    "tel" : "3815649551",
    "provincia" : "Buenos Aires"
}

print(cliente["nombre"])
print(cliente["edad"])
print(cliente["tel"])


#%%
producto = {}

producto["nombre"] = "Naranja"
producto["precio"] = 1000
print(producto)

pedido = {
    "id_pedido" : 10, 
    "estado" : "en proceso"
}
numero = pedido.get("id_pedido", 999)
print(f"el pedido {numero} es {pedido["estado"]}")

#%%
usuario = {"nombre" : "Maria"}

usuario["nombre"] = "Jose"

#borra el diccionario
usuario.clear()
usuario = []

#%%

carrito = {"Cafe": 10, "Medialuna" : 3}

retirado = carrito.pop("Medialuna")

print(carrito)

#%%

mi_diccionario = {
    "nombre" : "Sebastian",
    "apellido" : "Salomon",
    "edad" : 28,
    "mail" : "sebasalomoncn@gmail.com",
    "direccion" : "Diego de villarroel 767",
    "tel" : "3815649551",
    "Sueldo" : "200.000"
}

print(f"Mi nombre es {mi_diccionario['nombre']} tengo {mi_diccionario['edad']} años y vivo en {mi_diccionario['direccion']}.")

# %%

capitales = {
    "Argentina" : "Buenos Aires",
    "España" : "Madrid",
    "Francia" : "Paris",
}

for pais, ciudad in capitales.items():
    print(f"{pais} es el pais y {ciudad} es la capital.")
    
#%%
numero = [1,2,3,4,5,6,7,8,9,10]

for numero in range(1,11):
    print(numero)
# %%
numero = [1,2,3,4,5,6,7,8,9,10]

for numero in range(10,0,-1):
    print(numero)
# %%
numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for numero in range(1,21):
    if numero %2 == 0:
        print(numero)

numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for numero in range(2,22,2):
        print(numero)
        
# %%
suma = 0
for numero in range(1,11):
    suma = suma + numero 
print(suma)
    
# %%
palabra = input("Ingrese una palabra: ")

for letra in palabra:
    print(letra)
# %%
palabra = input("Ingrese una palabra: ")
letras = 0
for letra in palabra:
    letras += 1
print(f"la palabra {palabra} tiene {letras} letras..")
# %%
tabla = int(input("Ingrese un numero: "))
print(f"Tabla del {tabla}")
for i in range(1,11):
    print(f"{tabla} x {i} = {tabla * i} ")
# %%
