#%%
try:
    edad = int(input("Ingrese una edad: ")) 
    print(edad) 
except ValueError:
    print("El valor ingresado no es un numero")

# %%
try:
    respuesta = {"temperatura": 21}

    print(respuesta["humedad"])
except KeyError:
    print("Humedad no existe")
# %%
