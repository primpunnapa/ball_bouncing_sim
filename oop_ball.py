import turtle
import ball
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

    def draw_circle(self, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

    def move_circle(self, i):
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]

    def initilizing(self):
        for i in range(self.num_balls):
            self.xpos.append(random.randint(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.randint(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(random.randint(1, 0.01 * self.canvas_width))
            self.vy.append(random.randint(1, 0.01 * self.canvas_height))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def show_ball(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        while True:
            turtle.clear()
            for i in range(self.num_balls):
                self.draw_circle(self.ball_color[i], self.ball_radius, self.xpos[i], self.ypos[i])
                self.move_circle(i)
            turtle.update()


num_balls = int(input("Number of balls to simulate: "))
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
show = Ball(canvas_width, canvas_height, ball_radius, num_balls)
show.num_balls = num_balls
show.initilizing()
show.show_ball()
turtle.done()
