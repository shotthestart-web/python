import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon mandela")

board= turtle.Turtle()
board.speed("fastest")
board.hideturtle()
colors=["red","blue","green","yellow","pink","brown","white"]
for i in range(88):
    
    board.color(colors[i%len(colors)])
    board.width(2)
    board.forward(i*2)
    board.right(91)
board.penup()
board.goto(0,-66)
board.setheading(90)
board.pendown()
board.color("gold","yellow")
board.begain_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()
board.penup()
board.goto(0,0)
petal_colors=["lime","orange","green","yellow","pink","brown","white"]
for i in range (36):
    board.color(petal_colors[i%len(petal_colors)],
                petal_colors[(i+2)%len(petal_colors)])
    board.begain_fill()
    for j in range (4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)
turtle.done()