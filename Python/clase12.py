#%%
def saludo():
    print("Bienvenidos")
    print("Python")
    
saludo()
# %%


def recordatorio(nombre, hora):
    print(f"Hola {nombre}, tu turno es el jueves a las {hora}")
    
recordatorio("Sebastian", "17")
recordatorio("Sebastian", "17")
recordatorio("Sebastian", "17")
# %%

def calculo_total(precio, cantidad):
    print(f"El total es: {precio * cantidad}")
    
calculo_total(1500, 3)
calculo_total(2500, 4)
calculo_total(3500, 5)
# %%
def calculo_total(precio, cantidad):
    return precio * cantidad

total = calculo_total(1500, 3)
print(total)