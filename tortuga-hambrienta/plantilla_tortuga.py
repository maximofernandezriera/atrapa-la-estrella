# Actividad "La tortuga hambrienta" - 1º DAW - Programación
# Alumno/a: ____________________________
import random
import turtle

LIMITE = 250              # el campo va de -250 a 250 en x y en y
PASO = 20                 # píxeles que avanza la tortuga en cada pulsación
# TODO (Fase 5): constante LECHUGAS_PARA_GANAR

pantalla = turtle.Screen()
pantalla.setup(600, 600)
pantalla.title("La tortuga hambrienta - 1º DAW")
pantalla.bgcolor("lightgreen")

lapiz = turtle.Turtle()       # tortuga invisible para dibujar el campo
lapiz.hideturtle()
lapiz.speed(0)

tortuga = turtle.Turtle()     # la protagonista
# TODO (Fase 2): forma "turtle", color y penup()

# TODO (Fase 2): crea la tortuga 'lechuga' (forma "circle")
# TODO (Fase 5): crea la tortuga 'marcador' y la variable puntos


def dibujar_campo():
    # TODO (Fase 1): dibuja un cuadrado de lado LIMITE * 2 con un bucle for
    pass


def avanzar(direccion):
    # TODO (Fases 3 y 4): gira, avanza PASO y no salgas del campo
    pass


# Programa principal
dibujar_campo()
# TODO (Fase 3): asocia las flechas a funciones con pantalla.onkey(...)
pantalla.listen()

turtle.done()
