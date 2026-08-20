#%%
def especialidad_valida(especialidad, especialidades_validas):
    """
    Devuelve True si la especialidad es vailda y False si no lo es
    """
    return especialidad in especialidades_validas
    
def registrar_turno(nombre, especialidad, especialidades_validas):
    
    if especialidad_valida(especialidad, especialidades_validas)
        return{"nombre": nombre, "especialidad": especialidad, "atendido": False}
    return None

def contar_por_especialidad(turnos):
    conteo_especialidad = {}
     
    for turno in turnos:
        if turno["atendido"]:
            especialidad = turno["especialidad"]
            conteo_especialidad[especialidad] = conteo_especialidad.get(especialidad, 0) + 1 
            
    return contar_por_especialidad