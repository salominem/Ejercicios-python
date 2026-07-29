import tkinter as tk

ventana = tk.Tk()
ventana.title("Pollería MarAve")
ventana.geometry("350x250")

titulo = tk.Label(ventana, text="Sistema de Caja", font=("Arial",16))
titulo.pack(pady=10)

tk.Label(ventana, text="Inicio de Caja").pack()
entrada_inicio = tk.Entry(ventana)
entrada_inicio.pack()

tk.Label(ventana, text="Total de ventas").pack()
entrada_ventas = tk.Entry(ventana)
entrada_ventas.pack()

tk.Label(ventana, text="Total de gastos").pack()
entrada_gastos = tk.Entry(ventana)
entrada_gastos.pack()

def calcular():
    inicio = float(entrada_inicio.get())
    ventas = float(entrada_ventas.get())
    gastos = float(entrada_gastos.get())
    print(f"Inicio de caja : ${inicio:,.2f}")
    print(f"Ventas : ${ventas:,.2f}")
    print(f"Gastos : ${gastos:,.2f}")
    
boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack(pady=10)

ventana.mainloop()

