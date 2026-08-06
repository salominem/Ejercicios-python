#%%
pacientes_del_dia = [
{"nombre": "Marcos", "especialidad": "Pediatría", "edad": 8},
{"nombre": "Julia", "especialidad": "Cardiología", "edad": 45},
{"nombre": "Ana", "especialidad": "Pediatría", "edad": 5},
{"nombre": "Beto", "especialidad": "Traumatología", "edad": 30},
{"nombre": "Carla", "especialidad": "Cardiología", "edad": 60}
] 

for paciente in pacientes_del_dia:

    print(f"{paciente['nombre'].upper()}")

# %%
