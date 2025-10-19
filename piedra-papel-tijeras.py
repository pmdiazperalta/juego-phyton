nombre1 = input("¿Como se llamara el jugador1?")
nombre2 = input("¿Como se llamara el jugador2?")
                

jugador1 = input("¡Hola Jugador1! ¿que eliges? ¿Piedra,Papel o Tijeras: ")
jugador2 = input("¡Hola Jugador2! ¿que eliges? ¿Piedra,Papel o Tijeras: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"


if jugador1 == jugador2:
    print("ha sido un empate")

elif condicion1 or condicion2 or condicion3:
    print ("Ha ganado jugador 1")
          
else:
    print("Ha Ganddo Jugador 2")