import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)          
t.hideturtle()  

def draw_petal(color_name):
    t.fillcolor(color_name)
    t.begin_fill()
    
   
    for _ in range(2):
        t.circle(120, 60)  
        t.left(120)       
        
    t.end_fill()

colors = ["#FF2E63", "#08D9D6", "#252A34", "#FFDE7D", "#FF9F43", "#00CFB5", "#A3CB38", "#128C7E"]


number_of_petals = 36
rotation_angle = 360 / number_of_petals

for i in range(number_of_petals):
    
    current_color = colors[i % len(colors)]
    
    draw_petal(current_color)
    t.left(rotation_angle)  

t.penup()
t.goto(0, -25)  
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.circle(25)     
t.end_fill()
turtle.done()