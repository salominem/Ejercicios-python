#%%

# r = read : leer
# w = whrite : escribir
# a = append
# x = crea si no existe

#pasos...
archivo = open ("archivo.txt", "r", encoding="utf-8")
datos = archivo.read()
archivo.close()

archivo = open ("archivo.txt", "r", encoding="utf-8")
archivo.write("datos...\n")
archivo.close()

#%%
#arhivos
# /.... archivo01.py
# /.... archivo02.py
#clases 
# /.... clase01.py
# /.... clase02.py
# /.... clase03.py
# /.... clase04.py
# -> /.... clase10.py clase04.py ./clase02.py ../archivo/archivo01.py


archivo = open("../archivos/panchin.txt", "r")

datos = archivo.read()

archivo.close()

print(datos)


# %%
archivo = open("../archivos/panchin.txt", "a",encoding="utf-8")

archivo.write("Como estas\n")
archivo.write("todo bien?\n")
archivo.write("Como te fue\n")

archivo.close()
# %%

lista_tareas = ["revisar codigo \n",
                "revisar codigo \n",
                "revisar codigo \n",
                "revisar codigo \n",
                ]

archivo = open ("../archivos/lista_tareas.txt", "w", encoding="utf-8")

archivo.writelines(lista_tareas)
archivo.close()

# %%

with open ("../archivos/lista_tareas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("nueva tarea\n")


# %%

with open ("../archivos/lista_tareas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("panchin\n")

# %%
linea = "Seba, diego de villarroel, tucuman"

print(linea.split(","))