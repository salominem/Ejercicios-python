# primer Hola mundo
# print ("Hola Mundo")

# suma de dos enteros
# num1 = 1
# num2 = 2
# print(num1+ num2)

# esta mal
# num1 = input("Ingrese el primer numero: ")
# num2 = input("Ingrese el segundo numero: ")
# print(num1+ num2)

# esta bien
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# print(num1+ num2)

# grados = int(input("Cuantos grados hace? "))

# if grados >= 30 and grados < 50:
#     print("Me derrito")
# elif grados <= 29 and grados >= 15:
#     print("Esta lindo")
# else:
#     print("Hace frio")

#Imprime el 1 del [1,2]
# l = [1, 2, [1 , 2]]
# my_var = l[2][1]
# print(my_var)

#Imprime 1 y 12
# l = [1, 12 , True , "Hola mundo"]
# my_var = l[0:2]
# print(my_var)

#Imprime del true hasta el final...
# l = [1, 12 , True , "Hola mundo"]
# my_var = l[2:]
# print(my_var)

#Imprime 1, 12, true
# l = [1, 12 , True , "Hola mundo"]
# my_var = l[:3]
# print(my_var)

#Imprime de mi diccionario el valor basquet, porque pedimos como clave deporte.
# lista = {"nombre" : "sebastian",
#          "deporte" : "basquet",
#          "genero" : "masculino",
#          }
# print(lista["deporte"])


#Si la variable peli es igual a "Interestelar" imprime "Que buen gusto tienes!"
# peli = "Interestelar"
# if peli == "Interestelar":
#     print("Que buen gusto tienes!")


#Como peli no es igual a interestelar, entra al else e imprime "Vaya que lastima!"
# peli = "Hope"
# if peli == "Interestelar":
#     print("Que buen gusto tienes!")
# else:
#     print("Vaya que lastima!")


# numero = int(input("Ingrese un numero: "))

# if numero < 0:
#     print("Es negativo")
# elif numero > 0:
#     print("Es positivo")
# else:
#     print("Es cero")


#La edad comienza en 0 y mientras que edad sea menor a 18 se va a imprimir edad, edad ira sumando de 1 en 1 hasta llegar a 18.
# edad = 0
# while edad < 18:
#     edad = edad + 1
#     print(edad)
# print("Felicidades ya tienes 18!")

# secuencia = ["uno", "dos", "tres"]

# for elemento in secuencia:
#     print(elemento)

# for i in range(30,51):
#     print(i)

# ropa = ["pantalon", "remera", "media","pantalon"]
# ropa_sin_repetir = set(ropa)
# print(f"Tu ropero sin repetir ropa tiene: {ropa_sin_repetir}")

# for prenda in ropa:
#     print(f"Tu ropero tiene: {prenda}")