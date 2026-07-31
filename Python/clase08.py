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

respuestas = {
    "hola chimuelo" : "hola Sebastian!",
    "como estas?" : "bien y tu?",
    "yo estoy bien." : "me alegro Sebastian!",
    "que tal tu dia?" : "mi dia genial, aqui enseñandote a Programar!",
    "me siento triste" : "no pasa nada sebastian!, todos aveces nos sentimos asi, animo hermano!!",
    "chau chimuelo" : "chau Sebastian!, que tengas un lindo dia.",
}


while True:
    
    pregunta = input("Vos: ").strip().lower()
    
    if pregunta in respuestas:
        print(f"Chimuelo: {respuestas[pregunta]} ")
    else:
        print("No entendi.")
        break
        
        

# %%
