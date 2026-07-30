print("Jugadores de primera : Alberdi.")

jugadores = ["Seba","Lichi","Gian","Ismael","Anaya","Mirko","Ale","Godoy"]
dorsal = [8, 6, 7, 10, 12, 11, 9, 4]

for jugador, num in zip(jugadores, dorsal):
    print(f"{jugador} usa el numero {num}")

# %%

