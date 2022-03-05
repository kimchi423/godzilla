# def print1(ff):
#     print(f"{ff}안녕 하세요")
#
# # i = input("dlfmadmf dlqfur")
# # print1(i)
# import turtle
# import turtle as t
# t.shape("classic")
# win = turtle.Screen()
#
#
# def print1():
#     return 3
# print(print1())


rainbow_color = ["red","orange","yellow","green","blue","navy","purple"]

def draw_rainbow(t, rainbow_size, pen_size, x, y):
    for i in range(7):
        t.setheading(90)
        t.penup()
        t.pensize(pen_size)
        t.setpos(x + (rainbow_size / 2 - i * pen_size), y)
        t.pencolor(rainbow_color[i])
        t.pendown()
        t.speed(10)
        t.circle((rainbow_size / 2 - i * pen_size), 180)



import turtle

win = turtle.Screen()
win.screensize(100000,10000)
t = turtle.Turtle('turtle')
t.speed(0)

draw_rainbow(t,600,50,0,0)