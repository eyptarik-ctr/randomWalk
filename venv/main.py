import turtle as t
from random import*

char = t.Turtle()
char.pensize(20)
char.speed('fast')
t.colormode(255)
directions = [0,90,180,270]
for _ in range(100):
    r = randint(1,255)
    g = randint(1,255)
    b= randint(1,255)
    char.forward(50)
    char.setheading(choice(directions))
    char.color(r,g,b)
window = t.Screen()
window.mainloop()
