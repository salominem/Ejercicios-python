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
#1
especialidades = ["Clínica General", "Pediatria", "Traumatología", "Cardiología"]

#2
lista = [{
    "nombre": "Marcos",
    "especialidad": "Pediatría", 
    "atendido": False
},
{
    "nombre": "Julia",
    "especialidad": "Cardiología",
    "atendido": False
}]

#3

for paciente in lista:
    if paciente["especialidad"] in especialidades:
        paciente["atendido"] = True
        print(f"{paciente['nombre']} fue atendido.")
    else:
        print(f"{paciente['nombre']} quedó sin atender.")
        
#4
nombre = ""

while nombre != "cerrar":
    
    nombre = input("Ingrese paciente: ").strip().lower()
    if nombre != "cerrar":
        agregar_especialidad = input("Ingrese especialidad: ").strip()
        
        nuevo_paciente = {
            "nombre" : nombre,
            "especialidad" : agregar_especialidad,
            "atendido" : False
         }
        if nuevo_paciente["especialidad"] in especialidades:
            nuevo_paciente["atendido"] = True
        lista.append(nuevo_paciente)
    
#5

conteo = {}

for paciente in lista:
    if paciente["especialidad"] in especialidades:
        especialidad = paciente["especialidad"]
        conteo[especialidad] = conteo.get(especialidad, 0) + 1
#6

for paciente in lista:
    print(f"Paciente: {paciente['nombre']}")
    print(f"Especialidad: {paciente['especialidad']}")
    print(f"Estado: {paciente['atendido']}")
    print("-------------------------")
print(f"Resumen de pacientes atendidos por especialidad: {conteo}")
# %%
