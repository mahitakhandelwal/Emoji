import turtle

# 🙂
#***************************************************************
def simple1():
    root=turtle.Turtle()
    root.pensize(7)
    root.up()
    root.goto(0,-100)
    root.down()
    root.begin_fill()
    root.fillcolor("#ffe130")
    root.circle(100)
    root.end_fill()

    #muh
    root.up()
    root.goto(-60,-40)
    root.setheading(-60)
    root.pensize(3)
    root.width(1)
    root.down()
    root.begin_fill()
    root.fillcolor("Red")
    root.circle(70,120)
    root.end_fill()

    root.fillcolor("black")

    # eyes
    for i in range(-35 , 105 , 70):
        root.up()
        root.goto(i,35)
        root.setheading(0)
        root.down()
        root.begin_fill()
        root.circle(10)
        root.end_fill()

    turtle.mainloop()
#***************************************************************

# 😌
#***************************************************************
def simple2():
    root=turtle.Turtle()
    root.up()
    root.pensize(7)
    root.goto(0,-100)
    root.down()
    root.begin_fill()
    root.fillcolor("Orange")
    root.circle(100)
    root.end_fill()

    root.up()
    root.goto(-60,-40)
    root.setheading(-60)
    root.pensize(3)
    root.width(1)
    root.down()
    root.begin_fill()
    # root.fillcolor("Red")
    root.pensize(8)
    root.circle(70,120)
    root.end_fill()


    root.fillcolor("Black")

    root.pensize(3)
    # eyes
    for i in range(-60 , 80 ,  75):
        root.up()
        root.goto(i,35)
        root.setheading(-60)
        root.down()
        root.begin_fill()
        root.circle(25 , 120)
        root.end_fill()

    turtle.mainloop()
    #turtle.hide()  //screen will close u
#***************************************************************


# 🤩
#***************************************************************
def simple3():
    root=turtle.Turtle()
    root.up()
    root.pensize(7)
    root.goto(0,-100)
    root.down()
    root.begin_fill()
    root.fillcolor("Orange")
    root.circle(100)
    root.end_fill()

    root.up()
    root.goto(-60,-40)
    root.setheading(-60)
    root.width(1)
    root.down()
    root.begin_fill()
    root.fillcolor("Brown")
    root.circle(70,120)
    root.end_fill()


    root.fillcolor("black")


    # eyes
    root.color("Red")
    for i in range(-50 , 80 ,  65):
        root.up()
        root.goto(i,35)
        root.pendown()
        root.begin_fill()
        root.fillcolor("Red")
        for i in range(5):
            root.forward(50)           
            root.right(144)
        root.end_fill()               
# turtle.done()
        # root.setheading(-60)
        # root.down()
        # root.begin_fill()
        # root.circle(20 , 120)
        # root.end_fill()

    turtle.mainloop()

#***************************************************************


# confused with cross marks
#***************************************************************
def simple4():
    root=turtle.Turtle()
    root.pensize(5)
    root.up()
    root.goto(0,-100)
    root.down()
    root.begin_fill()
    root.fillcolor("Yellow")
    root.circle(100)
    root.end_fill()

#iska muh h 
    root.color("Black")
    root.up()
    root.pensize(4)
    root.goto(0,-75)
    root.pendown()
    root.setheading(0)
    root.begin_fill()
    root.fillcolor("Brown")
    root.circle(25)
    root.end_fill()

    root.up()
    root.pensize(10)
    root.goto(-45 , 45)
    root.pendown()
    root.setheading(-45)
    root.color = "Brown"
    root.forward(35)

    root.up()
    root.goto(-20 , 45)
    root.setheading(-135)
    root.pendown()
    root.forward(35)

    root.up()
    root.goto(45,45)
    root.pendown()
    root.setheading(-135)
    root.forward(35)

    root.up()
    root.goto(20 , 45)
    root.pendown()
    root.setheading(-45)
    root.forward(35)
    
    turtle.mainloop()
#***************************************************************


# 😆😆😆
#***************************************************************
def simple5():
    root=turtle.Turtle()
    root.pensize(7)
    root.up()
    root.goto(0,-100)
    root.down()
    root.begin_fill()
    root.fillcolor("Orange")
    root.circle(100)
    root.end_fill()

    root.up()
    root.pensize(2)
    root.goto(-60,-40)
    root.setheading(-60)
    root.width(1)
    root.down()
    root.begin_fill()
    root.fillcolor("Red")
    root.circle(70,120)
    root.end_fill()

    root.penup()
    root.fillcolor("black")  
    root.pensize(8)
    root.goto(-45,45)
    root.pendown()
    root.setheading(-45)
    root.forward(35)
    root.setheading(-135)
    root.forward(35)

    root.penup()
    root.fillcolor("black")  
    root.pensize(8)
    root.goto(45,45)
    root.pendown()
    root.setheading(-135)
    root.forward(35)
    root.setheading(-45)
    root.forward(35)
    turtle.mainloop()

#***************************************************************


# 😮😮😮😮
#***************************************************************
def simple6():
    root=turtle.Turtle()
    root.pensize(5)
    root.up()
    root.goto(0,-100)
    root.down()
    root.begin_fill()
    root.fillcolor("Yellow")
    root.circle(100)
    root.end_fill()

    root.color("Black")
    root.up()
    root.pensize(2)
    root.goto(0,-75)
    root.pendown()
    root.setheading(0)
    root.begin_fill()
    root.fillcolor("Red")
    root.circle(25)
    root.end_fill()

    root.color="Brown"
    root.up()
    root.pensize(4)
    root.goto(-40 , 20)
    root.pendown()
    root.setheading(0)
    root.begin_fill()
    root.fillcolor("White")
    root.circle(20)
    root.end_fill()

    root.up()
    root.pensize(4)
    root.goto(40,20)
    root.pendown()
    root.setheading(0)
    root.begin_fill()
    root.fillcolor("White")
    root.circle(20)
    root.end_fill()
    turtle.mainloop()
#***************************************************************


name = input("Enter your name : ")
name = name.upper()

if name[0] in ['B','J','K','G'] :
    simple3()
elif(name[0] in ['E','V','A','C','L'] ) : 
    simple2()
elif(name[0] in ['M','T','S','H','I'] ) :
    simple5()
elif(name[0] in ['Y','D','F','L','N','O']) : 
    simple6()
elif(name[0] in ['W','Z','R'] ) : 
    simple4()
else :
    simple1()

