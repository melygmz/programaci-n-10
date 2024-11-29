import random
import os

# Clase JuegoAdivinanza
class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validar_numero(self, numero):
        """Verifica si el número ingresado es menor, mayor o igual al número secreto."""
        if numero < self.numero_secreto:
            return "El número que ingresó es menor."
        elif numero > self.numero_secreto:
            return "El número que ingresó es mayor."
        else:
            return "Adivinó el número :) "

    def registrar_intento(self):
        """Aumenta el contador de intentos."""
        self.intentos += 1

    def reiniciar(self):
        """Reinicia el juego con un nuevo número secreto."""
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0


# Clase Jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def registrar_partida(self, intentos, gano):
        """Guarda el número de intentos y si ganó o perdió la partida."""
        self.historial.append((intentos, gano))

    def mostrar_estadisticas(self):
        """Muestra las estadísticas del jugador."""
        partidas_jugadas = len(self.historial)
        if partidas_jugadas == 0:
            print(f"{self.nombre}, no has jugado ninguna partida.")
            return
        
        aciertos = sum(1 for _, gano in self.historial if gano)
        porcentaje_aciertos = (aciertos / partidas_jugadas) * 100

        print(f"\nEstadísticas de {self.nombre}:")
        print(f"Partidas jugadas: {partidas_jugadas}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")


# Guardar estadísticas en un archivo
def guardar_estadisticas(jugadores):
    with open("estadisticas.txt", "w") as archivo:
        for jugador in jugadores:
            archivo.write(f"Nombre: {jugador.nombre}\n")
            archivo.write(f"Partidas jugadas: {len(jugador.historial)}\n")
            for intentos, gano in jugador.historial:
                archivo.write(f"{intentos} intentos - {'Ganó' if gano else 'Perdió'}\n")


# Cargar estadísticas desde un archivo
def cargar_estadisticas():
    jugadores = []
    if os.path.exists("estadisticas.txt"):
        with open("estadisticas.txt", "r") as archivo:
            lines = archivo.readlines()
            jugador = None
            for line in lines:
                if line.startswith("Nombre:"):
                    if jugador:
                        jugadores.append(jugador)
                    nombre = line.split(":")[1].strip()
                    jugador = Jugador(nombre)
                elif line.startswith("Partidas jugadas:"):
                    continue
                else:
                    intentos, resultado = line.split(" intentos - ")
                    gano = "Ganó" in resultado
                    jugador.registrar_partida(int(intentos), gano)
            if jugador:
                jugadores.append(jugador)
    return jugadores


# Mostrar menú
def mostrar_menu():
    print("\nMenú:")
    print("a) Comenzar nueva partida")
    print("b) Ver estadística de jugadores")
    print("c) Salir del juego")
    opcion = input("Elija una opción: ")
    return opcion


# Función principal del juego
def jugar():
    jugadores = cargar_estadisticas()

    if not jugadores:
        nombre = input("Ingrese su nombre: ")
        jugador = Jugador(nombre)
        jugadores.append(jugador)
    else:
        print("\nJugadores disponibles:")
        for idx, jugador in enumerate(jugadores, 1):
            print(f"{idx}. {jugador.nombre}")
        jugador_index = int(input("Elija el jugador: ")) - 1
        jugador = jugadores[jugador_index]

    while True:
        opcion = mostrar_menu()
        if opcion == "a":
            juego_actual = JuegoAdivinanza()
            print("\nComience el juego")
            while True:
                try:
                    numero = int(input("Adivina el número entre 1 y 100: "))
                except ValueError:
                    print("Ingrese un número válido.")
                    continue

                juego_actual.registrar_intento()
                resultado = juego_actual.validar_numero(numero)
                print(resultado)

                if resultado == "Adivinó el número":
                    jugador.registrar_partida(juego_actual.intentos, True)
                    print(f"Adivinaste el número en {juego_actual.intentos} intentos.")
                    break

        elif opcion == "b":
            for jugador in jugadores:
                jugador.mostrar_estadisticas()

        elif opcion == "c":
            print("Gracias por jugar")
            guardar_estadisticas(jugadores)
            break

        else:
            print("Opción no válida, inténtelo nuevamente.")


# Ejecución
if __name__ == "__main__":
    jugar()