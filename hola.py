
import turtle
t = turtle.Turtle()

t.forward(100)  # avanza
t.left(90)      # gira

angulos = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angulo in angulos:
    t.forward(100)
    t.left(angulo)

    rumbo = 0
for angulo in angulos:
    rumbo += angulo

print(rumbo)

rumbo = rumbo % 360


for i in range(5):
    t.forward(100)
    t.right(144)


    for i in range(12):
    t.forward(100)
    t.backward(100)
    t.right(30)




    t = turtle.Turtle()
print(type(t))






