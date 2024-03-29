import time
import turtle
from random import randrange 

BREAK_FLAG = False

# Создание окна
screen = turtle.Screen()
screen.title('Snake')
screen.bgcolor('blue')
screen.setup(650, 650)
screen.tracer(0)
# Границы игрового поля
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)
# Рисуем змейку
snake = []
for i in range(3):
	snake_segment = turtle.Turtle()
	snake_segment.shape('square')
	snake_segment.penup()
	if i > 0:
		snake_segment.color('gray')
	snake.append(snake_segment)
# Рисуем еду для змейки
food = turtle.Turtle()
food.shape('red')
food.penup()
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
# Контроллеры для змейки
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.listen()
# Новое создание еды для змейки и поглощение ее 
if snake[0].distance(food) < 10:
	food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
	snake_segment = turtle.Turtle()
	snake_segment.shape('square')
	snake_segment.color('gray')
	snake_segment.penup()
	snake_append(snake_segment)
for i in range(len(snake)-1, 0, 1):
	x = snake[i-1].xcor()
	y = snake[i-1].ycor()
	snake[i].goto(x,y)
snake[0].forward(20)
# Обновление
screen.update()
x_cor = snake[0].xcor()
y_cor = snake[0].ycor()
if x_cor > 300 or x_cor < -300:
   	screen.bgcolor('red')
    break
if y_cor > 300 or y_cor < -300:
        screen.bgcolor('red')
        break
for i in snake[1:]:
    i = i.position()
    if snake[0].distance(i) < 10:
    	BREAK_FLAG = True
    if BREAK_FLAG:
    	screen.bgcolor('red')
    	break
time.sleep(0.2)
