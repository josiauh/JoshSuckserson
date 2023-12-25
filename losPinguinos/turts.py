import turtle
import random
import tkinter
turtle.tracer(0)
# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("This is somebody's minecraft world.")

root = turtle.Screen()._root

img = tkinter.Image("photo", file="./icon.png")
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))

# Create a turtle
square_turtle = turtle.Turtle()
square_turtle.speed(2000)  # Faster speed
square_turtle.hideturtle()
square_turtle.goto(513,294)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        square_turtle.forward(size)
        square_turtle.right(90)

# Function to generate squares in a grid with custom colors
def generate_colored_square_grid(rows, cols, square_size, color_list):
    print("Finding a minecraft world...")
    square_turtle.goto(513,294)    
    for row in range(rows):
        for col in range(cols):
            # Calculate the position
            x = col * square_size
            y = -row * square_size  # Negative to start from the top

            square_turtle.penup()
            square_turtle.goto(x, y)
            square_turtle.pendown()

            # Set random color from the provided list
            color = random.choice(color_list)
            square_turtle.color(color)

            # Draw the square
            square_turtle.begin_fill()
            draw_square(square_size)
            square_turtle.end_fill()

# Set the size of each square
square_size = 20

# Set the number of rows and columns in the grid
rows = 10
cols = 10

# Define the list of colors
color_list = ["green", "brown", "blue", "blanched almond", "grey", "orange"]

# Function to clear the screen and regenerate the grid
def clear_and_regenerate(x, y):
    square_turtle.goto(513,294)
    square_turtle.clear()
    generate_colored_square_grid(rows, cols, square_size, color_list)
    write_message()

# Function to write the message at the top
def write_message():
    square_turtle.penup()
    square_turtle.goto(0, 200)
    square_turtle.pendown()
    square_turtle.color("white")  # Set color to black for the text
    square_turtle.write("This is somebody's Minecraft world", align="center", font=("Arial", 14, "normal"))
    square_turtle.penup()
    square_turtle.goto(0, -250)
    square_turtle.pendown()
    square_turtle.write("Click to find another one", align="center", font=("Arial", 14, "normal"))

# Bind the function to the click event
screen.onclick(clear_and_regenerate)

# Initial generation of the colored square grid and writing the message
generate_colored_square_grid(rows, cols, square_size, color_list)
write_message()

# Keep the window open
turtle.done()
