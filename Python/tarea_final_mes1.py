#%%
print("======Contador de Vocales======")

texto = "Boca mi buen amigo"

conteo = {
    'a': 0, 
    'e': 0,
    'i': 0, 
    'o': 0, 
    'u': 0
    }

for letra in texto.lower():
    if letra in conteo:
        conteo[letra] += 1 
print(conteo)
 # %%

numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for numero in range(2,22,2):
        print(numero)
# %%
