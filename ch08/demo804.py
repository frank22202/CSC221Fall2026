import random
import turtle

def draw_square(size, color) -> None:
    turtle.color(color)
    turtle.speed(1)
    turtle.shape("turtle")
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

# draw_square(200, 'red')
# draw_square(150, 'green')
# draw_square(100, 'purple')

for _ in range(10):
    draw_square(random.randint(1, 500), 'magenta')