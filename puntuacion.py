class Puntuacion:
    def __init__(self):
        self.puntos = 0

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad
        print(f"Puntuación actual: {self.puntos}")

    def reiniciar(self):
        self.puntos = 0
        print("Puntuación reiniciada.")

if __name__ == "__main__":
    p = Puntuacion()
    p.sumar_puntos(100)
    p.sumar_puntos(50)
    p.reiniciar()