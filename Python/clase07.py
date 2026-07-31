# #%%

# latitud = float(input("Ingrese la latitud: "))
# longitud = float(input("Ingrese la latitud: "))

# ubicacion = (latitud, longitud)

# print(f"La ubicacion es: {ubicacion}")

# # %%

# posicion = (100, 500)

# # pos_x = posicion[0]
# # pos_y = posicion[1]

# pos_x,pos_y = posicion

# pos_x += 15
# pos_y += 50

# print(f"Posicion original: {posicion} ")
# print(f"Posicion actual de x: {pos_x} ")
# print(f"Posicion actual de y: {pos_y} ")


# # %%

# catalogo = [("teclado",100),("mouse",50)]

# print(catalogo[1])

# producto = catalogo[1]

# nombre = producto[0]

# letra = nombre[0]

# print(producto, nombre, letra)

# # %%

# registro = ["ana" , "ana", "pedro", "ale", "santiago", "pedro"]

# asistencia = set(registro)

# print(registro)
# print(asistencia)

# # %%


# palabra_prohibida = {"spam", "virus", "estafa", "gratis"}

# comentario = input("Ingrese un comentario: ").strip().lower()

# if comentario in palabra_prohibida:
#     print(f"El comentario no es correcto!")
# else:
#     print("Comentario publicado con exito!")
    
# # %%

# suscriptores = {"seba@gmail.com", "maira@gmail.com"}

# print(suscriptores)

# suscriptores.add("pancho@gmail.com")

# print(suscriptores)

# suscriptores.discard("pancho@gmail.com")

# print(suscriptores)

# # %%

# sucursal_norte = ("mesa", "silla", "cama", "tele","lampara")
# sucursal_sur = ("mesa", "sofá", "cama", "tele")


# inventario = set(sucursal_norte + sucursal_sur)
# print(inventario)

# # %%


# tareas_totales = ("diseño", "programacion", "arte")
# completadas = {"diseño", "arte"}

# pendientes = set(tareas_totales) - completadas

# print(tareas_totales)
# print(pendientes)

# # %%


# usuario = "sebastian"
# puerto = 4000
# ip = "12.500000"

# datos = (usuario, puerto,ip)

# print(datos)

# # %%
# print("/////BAR EL JARDIN/////")

# menu = ("cafe", "medialuna", "tostado", "jugo")

# print("\nPedido de la mesa 1.")

# mesa =["cafe", "medialuna", "cafe"] 

# mesa.pop()
# mesa.append("tostado")

# print("Agregar una bebida: ")

# bebida = input("Desea agregar una bebida? ").strip().lower()


# if bebida in menu:
#     mesa.append(bebida)
#     print("bebida incorporada!") 
# else:
#     print("No existe la bebida.")

# pedido_final = set(mesa)

# print(f"\nTotal de ítems a cobrar: {len(mesa)}")
# print(f"Pedido completo: {mesa}")
# print(f"Preparación para cocina: {pedido_final}")






# # %%

# print("Ropero de Sebas")

# ropero = ["remera","pantalon","boxer","medias","remera",]

# ropero.append("campera")

# ropero_limpio = set(ropero)


# buscar = input("Buscar prenda: ")

# if buscar in ropero: 
#     print(f"Prenda encontrada, es: {buscar}")
# else:
#     print("Prenda no encontrada.")
    
# print(f"Total de prendas : {len(ropero_limpio)}")
# print(f"Las prendas serian: {ropero_limpio}")


# # %%

# print("Ropero de Sebas")

# ropero = ["remera","pantalon","boxer","medias","remera",]

# prenda = input("Ingrese la prenda: ").strip().lower()
# usuario = input("Quiere agregar o eliminar?").strip().lower()

# if usuario == "agregar":
#     ropero.append(prenda)
# elif usuario == "eliminar":
#     ropero.remove(prenda)
# else:
#     print("Prenda inexistente.")
    
# ropero_ordenado = set(ropero)
    
# print(f"Todas las prendas: {len(ropero)}")
# print(ropero)
# print(f"El ropero ordenado seria: {ropero_ordenado}")



# # %%
# print("Ropero de Sebas")

# ropero = ["remera","pantalon","boxer","medias","remera","campera"]

# while True: 
    
#         print("\n1.Ver prendas \n2.Agregar prenda \n3.Eliminar prenda \n4.Salir")
#         usuario = input("Eligue una opcion: ").strip().lower()
        
#         if usuario == "1":
#             print(f"Las prendas serian: {ropero}")
#         elif usuario == "2":
#             ropero.append("buzo")
#         elif usuario =="3":
#             ropero.remove("remera")
#         elif usuario == "4":
#             print("Saliendo...")
#             break

# # %%

# productos = ["coca","coca","galleta","fideo","azucar","yerba","jabon","shampoo","pepsi","aceite","sal","caldo","manteca","fideo",]

# while True:
#     print("////DRUGSTORE////")
#     print("\n1.Ver productos.. \n2.Agregar producto.. \n3.Eliminar producto.. \n4.Ver productos sin repetir.. \n5.Salir")
#     cliente = input("Eligue una opcion").strip().lower()
#     if cliente == "1":
#         print(f"Total de productos: {len(productos)}")
#         print(f"Los productos son: {productos}")
#     elif cliente == "2":
#         producto_nuevo = input("Ingrese el producto nuevo: ").strip().lower()
#         productos.append(producto_nuevo)
#         print("Producto agregado correctamente!")
#     elif cliente == "3":
#         borrar_producto = input("Que producto desea borrar?").strip().lower()
#         productos.remove(borrar_producto)
#         print("Producto eliminado correctamente!")
#     elif cliente == "4":
#         productos_unicos = set(productos)
#         print("\nLos productos sin repetir son: ")
#         print(f"Total de productos: {len(productos_unicos)} ")
#         print(productos_unicos)
#     elif cliente == "5":
#             print("Saliendo del sistema...")
#             break


# #%%

# # FOR

# numeros = [1,2,3,4,5,6,7,8]

# for indice in range(8):
#     print(numeros[indice])
    
# #%%

# for i in range(2,6):
#     print(i)

    
# # %%
# for i in range(6,0,-3):
#     print(i)
# # %%
# numeros = [1,2,3,4,5,6,7,8]
# for i in range(len(numeros)):
#     print(numeros[i])

# # %%

# letras = ["a","b","c"]

# for letra in letras:
#     print(letra)
# # %%

# coordenadas = (10, 50)

# for coordenada in coordenadas:
#     print(coordenada)
    
# # %%

# usuarios_unicos = {"usr_01","usr_02","usr_01","usr_04"}

# for usuario in usuarios_unicos:
#     print(usuario)
    
# # %%

# lista = ["usr_01","usr_02","usr_03","usr_04"]

# for indice, valor in enumerate(lista, 1):
#     print(indice,valor)

# # %%

# nombres = ["Ana", "Pedro", "Juan", "Maria"]
# edades = [20, 40, 35, 65]

# for nombre, edad in zip(nombres, edades):
#     print(f"{nombre} tiene {edad} años.") 


# # %%

# notas = [45, 75, 90, 20, 10]

# for nota in notas:
#     if nota > 70:
#         print(f"{nota} : Aprobado.")
#     else:
#         print(f"{nota} : Reprodado.")
# # %%

# reporte_ventas = [
#     ["Ana", 2000, 4000],
#     ["Pedro", 1000, 500],
#     ["Maria", 3000, 2500]
# ]

# for  fila in reporte_ventas:
#     nombre = fila[0]
#     print(f"Vendedor: {nombre}")

#     for venta in fila[1:]:
#         print(f"    - Ventas: ${venta}")    
        
# # %%

# intentos = 0

# while intentos < 3:
#     print(f"Intento nro: {intentos + 1}")
#     intentos += 1


# # %%

# edad = input("Ingrese su edad: ")

# while not edad.isdigit():
#     print("Esto no es un numero valido.")
    
#     edad = input("Ingrese nuevamente una edad: ")
    
# edad_num = int(edad)

# print(f"La edad es: {edad_num} ")
# # %%

# intentos_actual = 1
# maximos_intentos = 5
# conexion_exitosa = False

# while intentos_actual <= maximos_intentos and not conexion_exitosa:
#     print(f"Intentos para conectarse: {intentos_actual}")
#     conexion_exitosa = {intentos_actual == 5}
#     intentos_actual += 1
    
# if conexion_exitosa:
#     print("Conexion exitosa.")
# else:
#     print("No se pudo conectar al servidor.")


# # %%

# opcion1 = ""

# while opcion1 != "salir" and opcion1 != "3":
    
#     opcion1 = input("Menu [1] ver saldo [2] ver movimientos [3] salir")
    
#     if opcion1 == "1":
#         print("Tu saldo es: $100.000")
#     elif opcion1 == "2":
#         print("Ultimo movimiento: compra por $60.000")
        
# print("fin")

# print("=====Clinica=====")

# #1
# especialidades = ("Clínica General", "Pediatría", "Traumatología", "Cardiología")
# #2
# pacientes = ["Marcos", "Julia", "Marcos"]
# #3
# registro_unico = set(pacientes) 
# #4
# atendidos = []

# for paciente in pacientes:
#     if paciente in atendidos:
#         print(f"\n⚠ {paciente} Ya fue atendido")
#     else:
#         print(f"\n{paciente} está siendo atendido")
#         atendidos.append(paciente)
    
# #5
# pacientes_turno_tarde = []
# paciente_nuevo = ""

# while paciente_nuevo != "cerrar":
   
#     paciente_nuevo = input("\nIngrese un nuevo paciente o cerrar para salir. ").strip().lower()
#     if paciente_nuevo != "cerrar":
#         pacientes_turno_tarde.append(paciente_nuevo)
# #6
# print("=========Reporte final ==========")
# print(f"Total de pacientes atendidos: {len(pacientes)}")
# print(f"Total de pacientes unicos registrados: {len(registro_unico)}")
# print(f"Listado del turno tarde: {pacientes_turno_tarde}")



# numero = int(input("Ingresa un numero: "))
# print(f"Tabla de Multiplicar del {numero}: ")

# for i in range(1,11):
#     print(f"{numero} x {i} = {numero * i}")     
