
usuario1 = "sebastian" 
usuario2 = "jesus" 
print(f"Bienvenidos {usuario1} {usuario2}")

numero = 1
print(f"El numero es: {numero}")


nombre = input("ingrese el nombre de un jugador:  ")
print(f"El nombre del jugador que elegiste es: {nombre}", )

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))

suma = num1 + num2
print(f"La suma de los dos numeros es: {suma}") 

monto = float(input("ingrese un valor ")) 
print(monto + 10)


num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
resta = num1 - num2 

print(f"El resultado de la resta es: {resta}")

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
correo = input("Ingrese su correo: ")


print(f"Tu nombre es {nombre}, tu edad {edad} y tu correo es {correo} ")


numero1 = float(input("Ingrese un valor: "))
numero2 = float(input("Ingrese un valor: "))

suma = numero1 + numero2

print(f"La suma es: {suma}")


numero = int(input("Digite un numero: "))

if numero>0 :
    print ("El numero es positivo")
elif numero==0 : 
    print("El numero es 0")
else: 
    print("El numero es negativo")    
    
print("Fin del programa")   


edad = int(input("Digite su edad: "))

if edad>0 and edad <100:
    print("Edad correcta")
    if edad >=18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

edad = int(input("Digite su edad: "))

if 0<edad<100: 
    print("Edad correcta")
    if edad >=18: 
        print("Es mayor de edad")
    else: 
        print("Es menor de edad")
else:
    print("Edad incorrecta")        





numero = int(input("Ingrese un numero: "))

if numero %2 == 0 :
    print("El numero es par")
else:
    print("El numero es impar") 



edad = int(input("Ingrese su edad: "))

if edad >=18:
    print("Es mayor de edad")

elif edad >= 14 and edad <=17 :
    print("Es adolecente")
elif edad >= 5 and edad <= 13:
    print("Es niño")        
else:
    print("Es menor de edad")    



clavepordefecto = "seba123"
clave = input("ingrese su cotraseña: ")

if clavepordefecto == clave: 
    print("Contraseña correcta") 
    
else:
    print("Contraseña incorrecta")
    
    

salario = int(input("Ingrese su salario: "))
 
if salario < 18000:
    
    incremento = salario * 0.12
    total = salario + incremento
    print(f"Su salario con aumento del 12% es {total}")

elif salario >= 18000 and salario <= 30000:
    
    incremento1 = salario * 0.08
    total1 = salario + incremento1
    print(f"Su salario con aumento del 8% es: {total1}")      

elif salario >= 30000 and salario <= 50000:
    
    incremento2 = salario * 0.07
    total2 = salario + incremento2
    print(f"Su salario con aumento del 7% es: {total2}")  
    
elif salario >= 50000:
    
    incremento3 = salario * 0.06
    total3 = salario + incremento3
    print(f"Su salario con aumento del 6% es: {total3}") 
    
else: 
    print("No tiene aumento")     

 
numeros = [1, 2, 3]

res = numeros[2] + 2

print(f"El resultado de la resta es: {res}")


mi_diccionario = {
    "Nombre" : "Sebastian",
    "Apellido" : "Salomon",
    "Edad" : 28,
    "Direccion" : "Diego de villarroel 767",
    "Correo" : "sebasalomoncn@gmail.com",
    "Deporte" : "Basquet",
    "Perro" : "Pancho",
    "Gato1" : "Lil",
    "Gato2" : "Vaquita",
    "Gato3" : "Totita",
}
print(f"Mi deporte favorito es el {mi_diccionario['Deporte']} y mi perro se llama {mi_diccionario['Perro']} ")



mis_animales= ["vaquita", "totita","pancho", "Lobo"]

print(f"Mis dos gatitas son: {mis_animales[0]} y {mis_animales[1]} ... y mis dos perritos son: {mis_animales[2]} y {mis_animales[3]} ")


mi_local = {
    "Jefe" : "Aldo",
    "Edad" : 38,
    "Rubro" : "Polleria",
    "Direccion" : "Marcos paz 897",
    "Horario" : "Mañana"
}

print (f"Mi jefe es {mi_local['Jefe']} y trabajamos en una {mi_local['Rubro']} que esta ubicada en la {mi_local['Direccion']}")


numeros = [10, 2, 3, 5, 1]

print(sorted(numeros))



numero = int(input("Digite un numero: "))

if numero %2 == 0:
    print("Es PAR")
else:
    print("Es IMPAR")


nombre_administrador = "Sebastian Salomon"

nombre = input("Ingrese su usuario: ")

if nombre_administrador == nombre:
    print("Bienvenido Jefe!!")
else:
    print("Usuario incorrecto, intente nuevamente.")


x = 10 
y = 5

print(x == y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)
print(x != y)
print(x == y)

numero = int(input("Ingrese un numero: "))

if numero > 0 :
    print("Es numero ingresado es positivo")
elif numero < 0 :
    print("El numero ingresado es negativo")
else:
    print("El numero ingresado es cero") 
   

color = input("Ingrese un color: ").lower()

color_rojo = "rojo"
color_amarillo = "amarillo"
color_azul = "azul"


if color == color_rojo:
    print(f"Correcto {color_rojo} es un color primario ")
elif color == color_azul:
    print(f"Correcto {color_azul} es un color primario ")
elif color == color_amarillo: 
    print(f"Correcto {color_amarillo} es un color primario ")
else:
    print("No es un color primario")


lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)


for i in range(10): 
    if i == 8:
        break
    print(i)

artistas = ["Eminem", "Daddy Yankee", "50 cent", "Michael Jackson", "Gustavo Cerati"]

for artista in artistas:
    if artista == "Gustavo Cerati":
        break 
    print(artista) 


numeros = [1, 2, 3, 4, 5]

for i in numeros:
    if i == 5:
        break
    print(i)  
    
numeros = [1, 2, 3, 4, 5]

for i in numeros:
    if i == 2:
        break
    print(i)  


numero = 10

while numero >= 1:
    print(numero)
    numero -= 1

numero = 0

while numero <= 100:
    print(numero)
    numero += 5


numero = int(input("Ingrese un numero entero: "))

if numero > 0:
    print("El número es positivo")
elif numero == 0: 
    print("El número es 0")
else: 
    print("El número es negativo") 



numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))

if numero1 > numero2:
    print(f"El numero mayor es: {numero1} ")
elif numero1 == numero2:
    print("Ambos numeros son iguales!!")
else:
    print(f"El numero mayor es: {numero2}")


numero = int(input("Ingrese un numero entero: "))

if numero  %3 == 0 and numero %5 == 0: 
    print("Es multiplo de 3 y de 5")
elif numero %3 == 0:
    print("Solo es multiplo de 3")
elif numero %5 == 0:
    print("Solo es multiplo de 5")
else: 
    print("No es multiplo de 3 ni de 5")



Usuario = input("Ingrese su Usuario: ")
Contraseña = input("Ingrese su contraseña: ")

Administrador = "Sebastian"
Contraseña_1 = "pancho"

if Usuario == Administrador and Contraseña == Contraseña_1:
    print(f"Usuario correcto, bienvenido {Usuario}!")
else:
    print("Usuario incorrecto, intentelo nuevamente.")


administrador = "Sebastian"
contraseña_Ad = "pancho"
Intentos = 0 

while Intentos < 3:
    
    Usuario = input("Ingrese su Usuario: ")
    Contraseña = input("Ingrese su Contraseña: ")

    if Usuario == administrador and Contraseña == contraseña_Ad:
        print(f"Usuario correcto, bienvenido {administrador}")
        break
    elif Usuario != administrador :
        Intentos += 1 
        print(f"Usuario incorrecto. Intento {Intentos} de 3.")
    elif Contraseña != contraseña_Ad :
        Intentos += 1 
        print(f"Contraseña incorrecta. Intento {Intentos} de 3.")
  
if Intentos == 3:
    print("Cuenta bloqueada.")



id_jugador = 12345
intentos = 0

while intentos < 2:
    
    jugador = int(input("Ingrese id del jugador: "))
    
    if jugador == id_jugador:
        print(f"Bienvenido {id_jugador}")
        break
    elif jugador != id_jugador:
         intentos += 1 
         print(f"ID no encontrado, intento {intentos} de 2.")
    
        
if intentos == 2:
    print("Cuenta bloqueada")



nombre = input("Ingrese su nombre: ")
nota = int(input("Ingrese su nota: "))

if nota >= 6: 
    print(f"{nombre} está aprobado con {nota}")
else:
    print(f"{nombre} esta desparobado.")


i = 0 

while i < 10 :
    print(i)
    i += 1

Administrador = "Juan"
intento = 0

while intento < 3:
     
    usuario = input("Ingrese su usuario: ")
     
    if usuario == Administrador:
        print(f"Bienvenido {Administrador}")
        break
    elif usuario != Administrador:
        print(f"Usuario incorrecto, intento {intento} de 3. ")
        intento += 1
else:
    print("Cuenta bloqueada.")
    
numero = 1 

print("La tabla del 7 es: ")

while numero <= 10: 
    print(f"7 x {numero} = {7 * numero}")
    numero += 1
    

numero = 7

while numero <= 70:
    print(numero)
    numero += 7



tabla = int(input("que tabla desea ver? "))
contador = 1


while contador <= 10:
    print(f"{tabla} x {contador} = {tabla * contador}")
    contador += 1



numero = 0

if numero <= 10:
    print(numero)
    numero += 1










