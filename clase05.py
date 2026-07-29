#%%

numero = int(input("Ingresa un numero: "))
es_par = numero % 2

if es_par == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

# %%
temperatura = 50

if temperatura > 45:
    print("Me derrito")
# %%
temperatura = int(input("Ingrese la temperatura: "))

if temperatura >= 35:
    print("ME QUEMOOOOO")
elif temperatura <= 25 and temperatura >= 20:
    print("Está hermoso")
else:
    print("Esta frio")

# %%

numero1 = int(input("Ingrese un numero : "))
numero2 = int(input("Ingrese un numero : "))


if numero1 > numero2: 
    print("El primer numero ingresado es mayor")
elif numero2 > numero1:
    print("El segundo numero ingresado es mayor")
else:
    print("Los numeros ingresados son iguales")
    
    
    
# %%

pais = input("Ingrese el nombre de un Pais: ")

pais_campeon = "Argentina"

if pais == pais_campeon:
    print("ARGENTINA CAMPEON DEL MUNDO!!!!!")
else:
    print("España Campeon.")
    
# %%

copas = int(input("Ingrese el numero de copas"))

maximos_ganadores = 3

if copas >= maximos_ganadores:
    print("Uno de los paises que tiene mas copas.")
else:
    print("Tenes menos copas que los demas paises.")

# %%

numero = 0

while numero <= 10:
    print(numero)
    numero += 1
print("Fin del contador")


    
# %%


administrador = "Sebastian"
intentos = 0

while intentos < 3:
    usuario = input("Ingrese su usuario :")
    if usuario == administrador:
        print(f"Bienvenido {administrador} ")
        break
    if usuario != administrador:
        print(f"Usuario incorrecto. Vuelve a intentatrlo, intento {intentos} de 3.")
        intentos +=1
if intentos == 3:
    print("Cuenta bloqueada")
    

 # %%

campeon = "ARGENTINA"

intentos = 0 

while intentos < 4:
    pais = input("Ingrese el nombre del pais Campeon:")
    if pais == campeon:
        print(f"{campeon} ES EL CAMPEON DEL MUNDO")
        break
    if pais != campeon:
        print(f"{pais} no es el campeon")
        intentos += 1
if intentos == 4:
    print("Fin, no acertaste al Campeon")
# %%

print("Cuenta de steam: ")
cuenta = "salominem"
contraseña = "bocamibuenamigo"

intentos = 0

while intentos < 4:
    
    usuario = input("Ingrese su cuenta: ")
    contra = input("Ingrese su contraseña: ")
    
    if usuario == cuenta and contra == contraseña:
        print(f"Bienvenido {cuenta} ")
        break
    elif usuario != cuenta and contra != contraseña:
        print("Usuario y contraseña incorrecta, vuelve intentarlo.")
        intentos += 1
    elif usuario != cuenta:
        print("Usuario incorrecto, vuelve a intentarlo")
        intentos += 1
    elif contra != contraseña:
        print("Contraseña incorrecta, vuelve a intentarlo.")
        intentos += 1
        
if intentos == 4:
    print("Cuenta bloqueada.")
    
# %%

print("Contador del 1 al 10: ")
numero = 1

while numero <= 10:
    print(numero)
    numero += 1

# %%
print("Piedra, Papel o Tijeras: ")

jugador_1 = input("Jugador 1.. Piedra, Papel o Tijera? ").lower()
jugador_2 = input("Jugador 2.. Piedra, Papel o Tijera? ").lower()   

piedra = "piedra"
tijera = "tijera"
papel = "papel"

if jugador_1 == piedra and jugador_2 == tijera:
        print(f"Gana el jugador 1 con {piedra}") 
elif jugador_1 == tijera and jugador_2 == papel:
        print(f"Gana el jugador 1 con {tijera}")
elif jugador_1 == papel and jugador_2 == piedra:
        print(f"Gana el jugador 1 con {papel}")
elif jugador_2 == piedra and jugador_1 == tijera:
        print(f"Gana el jugador 2 con {piedra}") 
elif jugador_2 == tijera and jugador_1 == papel:
        print(f"Gana el jugador 2 con {tijera}")
elif jugador_2 == papel and jugador_1 == piedra:
        print(f"Gana el jugador 2 con {papel}")
if jugador_1 == jugador_2:
    print("Empate.")
print("Fin del juego.")

# %%
numero = int(input("Digite un numero: "))

if numero %2 == 0:
    print(f"{numero} Es par.")
else:
    print(f"{numero} Es impar")
# %%

numero = int(input("Digite un numero: "))

if numero %3 == 0 and numero %5 == 0:
    print(f"{numero} Es multiplo de 3 y de 5.")
elif numero %5 == 0:
    print(f"{numero} Solo es multiplo de 5.")
elif numero %3 == 0:
    print(f"{numero} Solo es multiplo de 3.")
else:
    print("No es multiplo de 3 ni de 5.")
# %%

# Escriba un programa que pregunte una
# y otra vez si desea continuar con el programa,
# siempre que se conteste exactamente sí (en minúsculas y con tilde).

seguir = "si"

pregunta = input("Desea continuar con el programa? ").lower()

while pregunta == seguir:
    
    pregunta = input("Desea continuar con el programa? ").lower()

print("Hasta la vista!.")


# %%
# Escriba un programa que pregunte una y otra vez 
# si desea terminar el programa, 
# salvo si se contesta exactamente SI (en mayúsculas y sin tilde).

terminar = "no"

pregunta = input("Desea terminar el programa?").lower()

while pregunta == terminar:
    
    pregunta = input("Desea terminar el programa?").lower()

print("!Hasta la vista!.")

# %%

pregunta = input("Desea terminar el programa?")

while pregunta == "n":
    pregunta = input("Desea terminar el programa?").lower()
print("¡Hasta la vista!")

# %%

pregunta = input("Desea continuar con el programa? ").lower()

while pregunta != "no":
    pregunta = input("Desea continuar con el programa? ").lower() 
print("!Hasta la vista!.")

# %%

print("La tabla del 3: ")

contador = 1

while contador <= 10:
    print(f"3 x {contador} = {contador *3} ")
    contador += 1
    

# %%

palabra1 = input("Ingresa la primer palabra de la empresa: ").strip()
palabra2 = input("Ingresa la segunda palabra de la empresa: ").strip()
palabra3 = input("Ingresa la tercer palabra de la empresa: ").strip()

acronimo = palabra1[0].upper() + palabra2[0].upper() + palabra3[0].upper()

print(f"El acronimo de {palabra1} {palabra2} {palabra3} es : {acronimo}")


# %%

palabra1 = input("Ingrese la primer palabra del club: ")
palabra2 = input("Ingrese la segunda palabra del club: ")
palabra3 = input("Ingrese la tercera palabra del club: ")
palabra4 = input("Ingrese la cuarta palabra del club: ")

acronimo = palabra1[0].upper() + palabra2[0].upper() + palabra3[0].upper() + palabra4[0].upper()

print(f"El acronimo de {palabra1} {palabra2} {palabra3} {palabra4} es : {acronimo} !!!! ")

#%%

numero1 = int(input("Ingrese un numero :"))
numero2 = int(input("Ingrese un segundo numero :"))

suma = numero1 + numero2 

print(f"la suma de los dos numeros es: {suma}")


# %%
