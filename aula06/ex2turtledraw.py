import turtle

t = turtle.Turtle()

with open ("drawing.txt",'r') as ficheiro:
    for i in ficheiro:
        if i == "UP\n":
            t.up()
        
        elif i == "DOWN\n":
            t.down()
        
        else: 
            t.goto(int(i.split(" ")[0]),int(i.split(" ")[1]))
        

turtle.Screen().exitonclick()

