print("=====Calculadora Salominem=====")

numero_1 = int(input("\nIngrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

print("\n1. Sumar (+)")
print("2. Restar (-)")
print("3. Multiplicar (*)")
print("4. Dividir (/)")

opcion = input("\nElige una opcion: ")
    
if opcion == "1":
    resultado = numero_1 + numero_2
    print(f"\n{numero_1} + {numero_2} = {resultado}")
    print(f"El resultado de la Suma es: {resultado} ")
elif opcion == "2":
    resultado = numero_1 - numero_2
    print(f"\n{numero_1} - {numero_2} = {resultado}")
    print(f"El resultado de la Resta es: {resultado} ")
elif opcion == "3":
    resultado = numero_1 * numero_2
    print(f"\n{numero_1} * {numero_2} = {resultado}")
    print(f"El resultado de la Multiplicacion es: {resultado} ")
elif opcion == "4":
    resultado = numero_1 / numero_2
    print(f"\n{numero_1} / {numero_2} = {resultado}")
    print(f"El resultado de la Division es: {resultado} ")

    
        
        

