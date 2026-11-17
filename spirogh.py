import turtle
import colorsys

# Configuration de l'écran
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spirograph")

# Configuration de la tortue
t = turtle.Turtle()
t.speed(50)
t.pensize(2)

# Dessiner 36 cercles multicolores
for i in range(36):
    hue = i / 36

    t.pencolor(colorsys.hsv_to_rgb(hue, 1, 1))
    t.circle(100)
    t.left(10)

# Terminer le dessin
t.hideturtle()
turtle.done()