import pygame as pg 
import math
import random

pg.init()

w_w=1500
w_h=900
x_c=w_w//2
y_c=w_h//2

n1x=x_c-20
n1y=y_c-20
n2x=x_c+20
n2y=y_c+20



middle=(x_c,y_c)
r=50
screen=pg.display.set_mode([w_w,w_h],pg.FULLSCREEN )
pg.display.set_caption('')

clock = pg.time.Clock()

a=0
b=0
c=0
c_speed=8       #speed of the object 
running=True

a1=random.random()-1
a1*=2
a2=random.random()-1
a2*=2
from math import sqrt
speed = (a1/sqrt(a1**2+a2**2), a2/sqrt(a1**2+a2**2))

while running:

    if random.random()>0.999:      #chance of changing directiory
        a1=random.random()-1
        a1*=2
        a2=random.random()-1
        a2*=2
        from math import sqrt
        speed = (a1/sqrt(a1**2+a2**2), a2/sqrt(a1**2+a2**2))


    if x_c > 1625-r//2 or x_c<r//2+25:
        speed = (-speed[0], speed[1])
    if y_c > 900 or y_c<r//2+20:
        speed = (speed[0], -speed[1])

    middle=(x_c,y_c)
    a = int((math.sin(pg.time.get_ticks() * 0.005) + 1) * 127.5)                #r
    b = int((math.sin(pg.time.get_ticks() * 0.005 + 2) + 1) * 127.5)            #g
    c = int((math.sin(pg.time.get_ticks() * 0.005 + 4) + 1) * 127.5)            #b   
    
    crc=pg.draw.rect(screen,(a,b,c),((x_c-50,y_c-50),(r,r)))

    pg.display.update()
    if random.random() > 0.997:     # chance of resetting the screen 
        screen.fill('black')

    x_c += speed[0]*c_speed
    y_c += speed[1]*c_speed

    for event in pg.event.get():

        if event.type==pg.QUIT:
            running=False
    clock.tick(160)



pg.quit()


# made by a coder(my friend) and a delitant(me)