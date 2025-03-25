import turtle  

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle pen
pen = turtle.Turtle()
pen.color("red")
pen.speed(3)

# Function to draw a heart
def draw_heart():
    pen.begin_fill()
    pen.fillcolor("red")
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Write text
def write_message():
    pen.up()
    pen.goto(-50, 200)
    pen.down()
    pen.color("black")
    pen.write("I Love You, Manisha!", font=("Arial", 16, "bold"))

# Draw the heart and write the message
pen.up()
pen.goto(0, -100)
pen.down()
draw_heart()
write_message()

# Hide the turtle and display
pen.hideturtle()
turtle.done()