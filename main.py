import turtle as t
import random 

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

guess = screen.textinput(title = "Turtle Racer", prompt= f"What turtle will win the race? {colors}: ").lower()
while guess not in colors:
    guess = screen.textinput(title = "Turtle Racer", prompt= f"What turtle will win the race? {colors}: ").lower()

y_cord = -100
all_turtles = []

for turtle_color in colors:
    racer = t.Turtle(shape = "turtle")
    racer.color(turtle_color)
    racer.penup()
    racer.goto(x = -375, y = y_cord)
    y_cord += 200/6
    all_turtles.append(racer)

def turtle_movement():
    for turtle in all_turtles:
        movement = random.randint(0, 100)
        turtle.forward(movement)

        if turtle.xcor() >= screen.window_width() // 2 - 30:
            print(f"{turtle.color()[0]} wins!")

            if guess == turtle.color()[0]:
                print(f"You were correct! You guessed {guess}!")
            else:
                print(f"You were wrong! You guessed {guess}!")
                
            return False
    
    return True

race_is_on = True
while race_is_on:
    race_is_on = turtle_movement()

screen.exitonclick()