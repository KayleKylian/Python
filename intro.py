import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for _ in range(80):
    for _ in range(2):
        t.forward(40)
        t.right(30)
        t.forward(50)
        t.right(30)
    t.backward(120)
    t.right(30)
    t.forward(120)
    t.right(5)