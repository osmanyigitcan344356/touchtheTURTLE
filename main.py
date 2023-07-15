import turtle

myscreen=turtle.Screen()
myscreen.bgcolor("green")
myscreen.title("MY SCREEN")

t=turtle.Turtle()
t.penup()
t.goto(0,270)
t.pendown()
t.write("GAME WİTH CONSOLE OF TURTLE",align="center",font=("Times New Roman",30,"normal"))
t.penup()

myturt=turtle.Turtle()
myturt.color("red")
myturt.shape("turtle")
myturt.shapesize(3,3,2)
myturt.penup()

score=0
score_turtle=turtle.Turtle()
score_turtle.color("black")
score_turtle.penup()
score_turtle.goto(0,250)
score_turtle.write(f"YOUR SCORE :{score}",align="center",font=("ıtaly",15,"normal"))

def update():
    score_turtle.clear()
    score_turtle.write(f"skorunuz : {score}")
def güncelleme():
    global score
    score+=1
    update()

def tıklama(x,y):
    global score
    score+=1
    update()

myturt.onclick(tıklama)


update()
countdown=10
timer=turtle.Turtle()
timer.goto(0,230)
timer.write(f"kalan zamanınız {countdown}")

def my_timer():
    global countdown
    timer.clear()
    timer.write(f"kalan zamanınız : {countdown}")
    countdown-=1
    if countdown>=0:
        timer.getscreen().ontimer(my_timer,1000)
myturt.onclick(tıklama)


update()

my_timer()






myturt.speed(1)
for x in range(15):
    myturt.hideturtle()
    myturt.right(60)
    myturt.forward(100)
    myturt.showturtle()






turtle.done()
