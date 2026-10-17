# Solución de referencia - Actividad "La tortuga hambrienta" (1º DAW - Programación)
import random
import turtle

# Constantes
LIMITE = 250              # el campo va de -250 a 250 en x y en y
PASO = 20                 # píxeles que avanza la tortuga en cada pulsación
LECHUGAS_PARA_GANAR = 5

# Ventana
pantalla = turtle.Screen()
pantalla.setup(600, 600)
pantalla.title("La tortuga hambrienta - 1º DAW")
pantalla.bgcolor("lightgreen")

# Tortugas auxiliares: una para dibujar y otra para escribir
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.speed(0)

marcador = turtle.Turtle()
marcador.hideturtle()
marcador.penup()

# Personajes
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("darkgreen")
tortuga.speed(0)
tortuga.penup()

lechuga = turtle.Turtle()
lechuga.shape("circle")
lechuga.color("limegreen")
lechuga.speed(0)
lechuga.penup()

puntos = 0


def dibujar_campo():
    """Fase 1: dibuja el borde del campo con un bucle."""
    lapiz.penup()
    lapiz.goto(-LIMITE, -LIMITE)
    lapiz.pendown()
    lapiz.pensize(5)
    lapiz.color("saddlebrown")
    for lado in range(4):
        lapiz.forward(LIMITE * 2)
        lapiz.left(90)


def colocar_lechuga():
    """Fase 2: pone la lechuga en un sitio al azar dentro del campo."""
    x = random.randint(-LIMITE + 20, LIMITE - 20)
    y = random.randint(-LIMITE + 20, LIMITE - 20)
    lechuga.goto(x, y)


def escribir_marcador(texto):
    marcador.clear()
    marcador.goto(0, LIMITE + 10)
    marcador.write(texto, align="center", font=("Arial", 20, "bold"))


def comprobar_lechuga():
    """Fase 5: si la tortuga llega a la lechuga, suma un punto."""
    global puntos
    if tortuga.distance(lechuga) < PASO:
        puntos += 1
        if puntos == LECHUGAS_PARA_GANAR:
            lechuga.hideturtle()
            escribir_marcador("¡Has ganado! Te has comido " + str(puntos) + " lechugas")
        else:
            colocar_lechuga()
            escribir_marcador("Lechugas: " + str(puntos))


def avanzar(direccion):
    """Fases 3 y 4: gira hacia 'direccion', avanza y no sale del campo."""
    if puntos == LECHUGAS_PARA_GANAR:
        return                      # la partida ha terminado
    tortuga.setheading(direccion)
    tortuga.forward(PASO)
    if abs(tortuga.xcor()) > LIMITE - 10 or abs(tortuga.ycor()) > LIMITE - 10:
        tortuga.backward(PASO)      # se saldría: deshacemos el paso
    comprobar_lechuga()


def arriba():
    avanzar(90)


def abajo():
    avanzar(270)


def izquierda():
    avanzar(180)


def derecha():
    avanzar(0)


# Programa principal
dibujar_campo()
colocar_lechuga()
escribir_marcador("Lechugas: 0")

pantalla.onkey(arriba, "Up")
pantalla.onkey(abajo, "Down")
pantalla.onkey(izquierda, "Left")
pantalla.onkey(derecha, "Right")
pantalla.listen()

turtle.done()
