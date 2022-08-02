#call turtle
import turtle
greeny = turtle.Turtle()
greeny.shape('turtle')
#set colors 
colors = ['red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'magenta']
turtle.bgcolor('black') #BG color black
#Geometric Octogon with repeat
for n in range(10):
    for i in range(8):
        greeny.right(45)
        greeny.forward(100)
        greeny.color(colors[i])#pick color at position i
    greeny.right(36) #turn greeny
#pen up and color
greeny.penup()
greeny.color('white')
#draw 10 circles
for i in range(10):
    greeny.forward(220)
    greeny.pendown()
    greeny.circle(10)
    greeny.penup()
    greeny.backward(220)
    greeny.right(36)
greeny.right(18)
for i in range(10):
    greeny.forward(270)
    greeny.pendown()
    greeny.circle(10)
    greeny.penup()
    greeny.backward(270)
    greeny.right(36)
