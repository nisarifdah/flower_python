import turtle as tur
import colorsys as css

tur.setup(800, 800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")

for j in range(15):
    for i in range(15):
        tur.color(css.hsv_to_rgb(i / 15, j / 25, 1))
        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)

tur.hideturtle()
tur.done()


## https://www.youtube.com/watch?v=1aQ7nTpLQHA
## https://medium.com/@rohitsaroj29/how-to-turn-your-python-script-into-an-executable-file-d64edb13c2d4