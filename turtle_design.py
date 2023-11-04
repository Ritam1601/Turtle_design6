import turtle as t
from time import sleep
#sleep(2)
t.pencolor('purple')
t.pensize(2)
t.bgcolor('black')
t.speed('fastest')
def poly(L):
	for i in range(4):
		t.fd(L)
		t.rt(90)
	return
for f in range(80):
	poly(100)
	t.rt(5)
t.exitonclick()


	