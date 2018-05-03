import turtle
import random

#bob=turtle.turtle():
#for i in range(20)
#	bob.fd(50)

# Create play area
play_area =turtle.Screen()
play_area.screensize(680,680)
print(play_area)
turtle.setup(w=680,l=680)

snake=turtle.turtle
snake.setposition(-48,-460)
snake.fd(200)

def turnleft():
	snake.lt((90))
def turnright():
	snake.rt(90))
play_area.listen()
play_area.onkey(turnleft,"left")
play_area.onkey(TURNRIGHT,"right")
print(snake)

while True:
	snake.fd(1)
