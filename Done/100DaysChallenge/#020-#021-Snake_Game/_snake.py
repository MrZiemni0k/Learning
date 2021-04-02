from turtle import Turtle

MOVE_DISTANCE = [20]

class Snake():
    
    def __init__(self):
        self.snake_body = []
        self.start_snake_body()

    def start_snake_body(self):
        x_cord = 0
        for _ in range(3):
            _snake = Turtle(shape="square")
            _snake.color(25, 74, 38)
            _snake.penup()
            _snake.goto(x_cord,0)
            x_cord -= 20
            self.snake_body.append(_snake)
            self.snake_body[0].color(20, 107, 43)
    def add_body(self):
            _snake = Turtle(shape="square")
            _snake.color(25, 74, 38)
            _snake.penup()
            _snake.goto(self.snake_body[-1].pos())
            self.snake_body.append(_snake)
    def move(self,screen):  
        for x in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[x].goto(self.snake_body[x-1].pos())

        screen.onkey(fun=self.go_left,key='Left')
        screen.onkey(fun=self.go_right,key='Right')
        screen.onkey(fun=self.go_up,key='Up')
        screen.onkey(fun=self.go_down,key='Down')
        self.snake_body[0].forward(MOVE_DISTANCE[0])
        
    def go_left(self):
        if self.snake_body[0].heading() != 0: #Not going right
           self.snake_body[0].setheading(180)
    
    def go_right(self):
        if self.snake_body[0].heading() != 180: #Not going left
           self.snake_body[0].setheading(0)

    def go_up(self):
        if self.snake_body[0].heading() != 270: #Not going down
           self.snake_body[0].setheading(90)
    
    def go_down(self):
        if self.snake_body[0].heading() != 90: #Not going up
           self.snake_body[0].setheading(270)    
