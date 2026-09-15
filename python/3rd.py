##a = int(input("첫번째 값 :"))
##b = int(input("두번째 값 :"))
##c = int(input("세번째 값 :"))

##print(a, "*", b, "*", c, "=" , a*b*c)
##print(a, "/", b, "/", c, "=" , a/b/c)
##print(a, "+", b, "+", c, "=" , a+b+c)
##print(a, "-", b, "-", c, "=" , a-b-c)

##data = '안녕'+\
##'하세요?' +\
##'파이썬!'
##print(data)


##import turtle

##t = turtle.Turtle()
##t.speed(5)
##t.pensize(10)
##t.pencolor("blue")



##t.shape("circle")
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)



##turtle.done()

import turtle
import random

##함수 선언 부분 ##
def screenLeftClick(x,y):
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.goto(x,y)

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
        global r,g,b
        tSize = random.randrange(1,10)
        turtle.shapesize(tSize)
        r=random.random()
        g=random.random()
        b=random.random()
        turtle.pencolor((r,g,b))
##변수 선언 부분##
pensize = 10
r, g, b = 0.0, 0.0, 0.0

##메인 코드 부분##
turtle.title("거북이로 그림그리기")
turtle.shape("turtle")
turtle.pensize(pensize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)
turtle.onscreenclick(screenMidClick, 2)
turtle.done()