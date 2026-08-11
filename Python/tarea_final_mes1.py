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
especialidades = ["Clínica General", "Pediatría", "Traumatología", "Cardiología"]

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


#%%
print("=====Club Juan Bautista Alberdi=====")
j_b_alberdi = ("basquet","futbol","voley","handball") 
print("Deportes disponibles: ")
print(j_b_alberdi)

lista_jugadores = []

opcion = ""

while opcion != "4":
    print("\n==Menu==")
    print("\n1. Ver lista.")
    print("2. Agregar jugador.")
    print("3. Eliminar jugador.")
    print("4. Salir.")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        print("\nLista de jugadores y su deporte: ")
        for jugador in lista_jugadores:
            print(f"{jugador['nombre']} - {jugador['deporte']}")
        
    elif opcion == "2":
        nombre = input("Ingrese nombre del jugador: ").lower().strip()
        deporte = input("Ingrese para que deporte desea inscribirlo: ").lower().strip() 
        nuevo_jugador = {
            "nombre" : nombre,
            "deporte" : deporte
        }      
        lista_jugadores.append(nuevo_jugador)
        print("\nJugador agregado con exito!")
        
    elif opcion == "3":
        eliminar = input("Que jugador desea eliminar? ")
        for jugador in lista_jugadores:
            if jugador["nombre"] == eliminar:
                lista.remove(jugador)
                print("\nJugador eliminado con exito!")
                break
                
    elif opcion == "4":
        print("Saliendo del sistema...")
    else:
        print("Opcion invalida, intente nuevamente.")
        
        
    
# %%

frase = "Me gusta progamar en python. Es genial"

conteo = {"a" : 0,"e" : 0,"i" : 0,"o" : 0,"u" : 0,}

for letra in frase:
    if letra in conteo:
        conteo[letra] += 1
print(conteo)
# %%

especialidades = ("Clínica General", "Pediatría", "Traumatología", "Cardiología")

pacientes = [
    {"nombre" : "Marcos", "especialidad" : "Pediatría", "atendido" : False},
    {"nombre" : "Julia", "especialidad" : "Cardiología", "atendido" : False}
]

for paciente in pacientes:
    if paciente["especialidad"] in especialidades:
        paciente["atendido"] = True
        print(f"{paciente['nombre']} fue atendido en {paciente['especialidad']}")
    else:
        print(f"{paciente['nombre']} no fue atendido debido que la especialidad {paciente['especialidad']} no esta en la lista")
        
nombre_pacientes = ""
corte = "cerrar"

while nombre_pacientes.lower() != corte:
    nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
    
    if nombre_paciente == corte:
        break
    especialidad_paciente = input("Ingrese la especialidad: ").strip().title()
        
    nuevo_paciente = {"nombre": nombre_paciente, "especialidad" : especialidad_paciente, "atendido" : False}
        
    if especialidad_paciente in especialidades:
        nuevo_paciente["atendido"] = True
    else:
        print(f"{nombre_paciente} no fue atendido debido que la especialidad {especialidad_paciente} no esta en la lista")
    
    pacientes.append(nuevo_paciente)
    
    
    
    conteo_especialidad = {}
    for paciente in pacientes:
        if paciente["atendido"]:
            especialidad = paciente["especialidad"]
            conteo_especialidad[especialidad] = conteo_especialidad.get(especialidad, 0) + 1
            
print("Reporte final")

for paciente in pacientes:
    if paciente["atendido"]:
        estado = "Atendido"
    else:
        estado = "Pendiente"
    
    estado = "Atendido" if paciente["atendido"] else "Pendiente"
        
    print(f"{paciente ['nombre']}: {estado}")
    
print("Resumen de cantidad de pacientes ") 
for especialidad, cantidad in conteo_especialidad.items():
    print(f"{especialidad}: {cantidad} pacientes atendidos")

    
# %%

datos = {"numero" : 1, "nombre" : "Julio"}

copia = datos.copy()

copia["numero"] = 2

print(copia)
print(datos)
# %%

precios = [2500, 1800, 3000]

precios_con_descuentos = []

for precio in precios:
    precios_con_descuentos.append(precio * 0.9)
    
print(precios_con_descuentos)

# %%

precios_con_descuentos = [precio * 0.9 for precio in precios]
print(precios_con_descuentos)

# %%
clientes = ["Ana", "Jorge", "Julia"]

clientes_may = [cliente.upper() for cliente in clientes]

print(clientes_may)
# %%

pacientes = [
    {"nombre" : "Marcos", "especialidad" : "Pediatría", "atendido" : False},
    {"nombre" : "Julia", "especialidad" : "Cardiología", "atendido" : False}
]

nombres = [paciente["nombre"] for paciente in pacientes]
print(nombres)
# %%

inventario = [("cafe", 45), ("medialuna", 0), ("tostado", 10)]

productos = [ producto for producto, cantidad in inventario if cantidad > 0 ]
print(productos)

# %%

pacientes_del_dia = [
{"nombre": "Marcos", "especialidad": "Pediatría", "edad": 8},
{"nombre": "Julia", "especialidad": "Cardiología", "edad": 45},
{"nombre": "Ana", "especialidad": "Pediatría", "edad": 5},
{"nombre": "Beto", "especialidad": "Traumatología", "edad": 30},
{"nombre": "Carla", "especialidad": "Cardiología", "edad": 60}
]

pacientes_mayuscula = [paciente["nombre"].upper() for paciente in pacientes_del_dia]
print(pacientes_mayuscula) 

pacientes_mayores = [paciente["nombre"] for paciente in pacientes_del_dia if paciente["edad"] > 18]  
print(pacientes_mayores)

especialidades = [paciente["nombre"] for paciente in pacientes_del_dia if paciente["especialidad"]]
print(especialidades)
