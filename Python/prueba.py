productos = ["coca","coca","galleta","fideo","azucar","yerba","jabon","shampoo","pepsi","aceite","sal","caldo","manteca","fideo",]

while True:
    print("////DRUGSTORE////")
    print("1.Ver productos.. \n2.Agregar producto.. \n3.Eliminar producto.. \n4.Ver productos sin repetir.. \n5.Salir")
    cliente = input("Eligue una opcion: ").strip().lower()
    if cliente == "1":
        print(f"Total de productos: {len(productos)}")
        print(f"Los productos son: {productos}")
    elif cliente == "2":
        producto_nuevo = input("Ingrese el producto nuevo: ").strip().lower()
        productos.append(producto_nuevo)
        print("Producto agregado correctamente!")
    elif cliente == "3":
        borrar_producto = input("Que producto desea borrar?").strip().lower()
        productos.remove(borrar_producto)
        print("Producto eliminado correctamente!")
    elif cliente == "4":
        productos_unicos = set(productos)
        print("\nLos productos sin repetir son: ")
        print(f"Total de productos: {len(productos_unicos)} ")
        print(productos_unicos)
    elif cliente == "5":
            print("Saliendo del sistema...")
            break
        
        