from turtle import *
from math import *

# Configuração inicial
speed(0)
bgcolor("black")
goto(0,-40)

# Desenha as pétalas da flor
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6,90), lt(90)
        circle(150-j*6,90), rt(180)
    circle(40,24)

# Configuração para o centro da flor
color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
angulo_dourado = 137.508
fi = angulo_dourado * (pi/180)

# Desenha o centro da flor usando a proporção áurea
for i in range(140):
    r = 4 * sqrt(i)
    theta = i * fi
    x = r * cos(theta)
    y = r * sin(theta)
    penup(), goto(x,y)
    setheading(i * angulo_dourado)
    pendown(), stamp()

def desenhar_circulo(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(3), end_fill()

def desenhar_N(x, y):
    posicoes_n = [(x, y), (x, y+4), (x, y+8), (x, y+12), (x, y+16),
                  (x, y+20), (x, y+24), (x+3, y+21), (x+6, y+18),
                  (x+9, y+15), (x+12, y+12), (x+15, y+9), (x+18, y+6),
                  (x+21, y+3), (x+24, y), (x+24, y+4), (x+24, y+8),
                  (x+24, y+12), (x+24, y+16), (x+24, y+20), (x+24, y+24)]

    for pos in posicoes_n:
        desenhar_circulo(*pos)

def desenhar_A(x, y):
    posicoes_a = [(x, y), (x+2, y+4), (x+4, y+8), (x+6, y+12),
                  (x+8, y+16), (x+10, y+20), (x+12, y+24), (x+14, y+20),
                  (x+16, y+16), (x+18, y+12), (x+20, y+8), (x+22, y+4),
                  (x+24, y), (x+8, y+8), (x+12, y+8), (x+16, y+8)]

    for pos in posicoes_a:
        desenhar_circulo(*pos)

# Escreve "ANA" no centro da flor
desenhar_A(-36, -10), desenhar_N(-6, -10), desenhar_A(24, -10)
hideturtle()
done()