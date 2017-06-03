import turtle

foo = turtle.Turtle()
foo.shape("square")
foo.shapesize(0.4,0.4,0)
foo.penup()

foo.speed(0)
foo.color("gray")

width = 40
height = 40

originx = -1*(width/2)*10
originy = -1*(height/2)*10

grid = []

for j in range(0,height):
    row = []
    for i in range(0,width):
        row.append(0)
    grid.append(row)

#grid[0][0] = 1
ax,ay = float(0),float(0)
bx,by = float(30),float(17)

dx = bx - ax
dy = by - ay

print dx,dy

if abs(dx) > abs(dy):
    steps = abs(dx)
else:
    steps = abs(dy)

xinc = dx / float(steps)
yinc = dy / float(steps)

x,y = ax,ay

grid[int(round(ax))][int(round(ay))] = 1
for p in range(0,int(steps)):
    x += xinc
    y += yinc
    grid[int(round(x))][int(round(y))] = 1

#grid[5][5] = 1

for j in range(0,height):
    for i in range(0,width):

        foo.setpos(10*i + originx, 10*j + originy)
        if grid[i][j] == 1:
            foo.color("black")
        foo.stamp()
        foo.color("gray")

