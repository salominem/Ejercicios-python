# print("Jugadores de primera : Alberdi.")

# jugadores = ["Seba","Lichi","Gian","Ismael","Anaya","Mirko","Ale","Godoy"]
# dorsal = [8, 6, 7, 10, 12, 11, 9, 4]

# for jugador, num in zip(jugadores, dorsal):
#     print(f"{jugador} usa el numero {num}")

# %%


respuestas = {
    "hola chimuelo" : "hola Sebastian!",
    "como estas?" : "bien y tu?",
    "yo estoy bien" : "me alegro Sebastian!",
    "me alegro por vos chimuelo" : "gracias sebastian!",
    "que tal tu dia?" : "mi dia genial, aqui enseñandote a Programar!",
    "me siento triste" : "no pasa nada sebastian!, todos aveces nos sentimos asi, animo hermano!!",
    "hoy juega boquita" : "que grande, hoy gana boquita",
    "quiero empezar el gimnasio" : "y que esperas? que te den un premio?",
    "que calor hace hoy" : "la verdad que si, esta haciendo mucho calor",
    "que frio hace hoy" : "la verdad que si, está re fresco",
    "hoy juego partido" : "que grande!!!, dedicame un par de triples jajaj",
    "tenemos que ganar si o si" : "a ponerte las pilas entonces!!",
    "extraño a mi perrito" : "el seguramente te debe estar extrañando tambien!",
    "quiero ser el mejor" : "y vas a ser el mejor.",
    "tengo que trabajar" : "me parece bien, hay que trabajar para tener platita",
    "estoy feliz hoy" : "esoo bien ahi papaaa, asi tiene que ser siempre!",
    "quiero seguir programando" : "me parece perfecto, hay que mejorar dia a dia!",
    "sale lolcito" : "aprende a jugar bronce jajaja",
    "estoy practicando un sistema de bar" : "perfecto y como te está yendo?",
    "vendi un sistema" : "genial que bueno che!",
    "quiero trabajar de programador" : "tranqui, vas a conseguir un trabajo",
    "chau chimuelo" : "chau Sebastian!, que tengas un lindo dia.",
}

while True:
    
    pregunta = input("Vos: ").strip().lower()
    
    if pregunta in respuestas:
        print(f"Chimuelo: {respuestas[pregunta]} ")
        if pregunta == "chau chimuelo":
            break
    else:
        print("No entendi.")
        