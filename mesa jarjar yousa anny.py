import turtle


space=turtle.Screen()
space.bgcolor("black")
space.listen()

red_squdrin_leader=turtle.Turtle()
jarjar=turtle.Turtle()
anakin=turtle.Turtle()
obiwankenobi=turtle.Turtle()
red_squadrin = [turtle.Turtle() for i in range(40)]
anakin.pu()
obiwankenobi.pu()
jarjar.pu()
red_squdrin_leader.pu()
anakin.color("tan")
jarjar.color("darkorange")
obiwankenobi.color("peru")
red_squdrin_leader.color("red")

for i in red_squadrin:
    i.pu()
    i.color("red")
    i.speed()
for i in range(40):
    if i <20:
        red_squadrin[i].goto(-90+(6.75*i),100-(4.5*i))
    else:
        red_squadrin[i].goto(38.25-(6.75*(i-20)),0-(4.5*(i-20)))


def feet(x,y):
    obiwankenobi.goto(x,y)
    anakin.goto(obiwankenobi.xcor()-10,obiwankenobi.ycor())
    jarjar.goto(anakin.xcor()-10,anakin.ycor()-10)
def poop(x,y):
    red_squdrin_leader.goto(x,y)
    for i in range(40):
        if i <20:
            red_squadrin[i].goto((-90+x)+(6.75*i),(100+y)-(4.5*i))
        else:
            red_squadrin[i].goto((38.25+x)-(6.75*(i-20)),(0+y)-(4.5*(i-20)))
red_squdrin_leader.onrelease(poop)               
obiwankenobi.onrelease(feet)
turtle.done()