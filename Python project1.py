from turtle import*
import colorsys
bgcolor("black")
tracer(500)

def drawn():
    h=0
    for i in range(100):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.5
        penup()
        goto(0,0)
        pendown()
        color("white")
        fillcolor(c)
        begin_fill()
        right(98)
        circle(i,12)
        fd(i)
        left(29)
        for j in range(129):
            fd(i)
            circle(j,129,steps=2)
            end_fill()
drawn()
done()
