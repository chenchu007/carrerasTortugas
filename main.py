import turtle

class Circuito():
    corredores = []
    __posStartY = [-30,-10,10,30]
    __colorTurtle = ['red','blue','green','orange']
    #pantalla

    def __init__(self,width,height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgray')
        self.__startline = -width/2 + 20
        self.__finishline = height - 20
        
        self.__createRunners()

    def __createRunners(self):
        for jugador in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape('turtle')
            new_turtle.color(self.__colorTurtle[jugador])
            new_turtle.setpos(self.__startline, self.__posStartY[jugador])
            self.corredores.append(new_turtle)


if __name__ == '__main__':
    circuito = Circuito(640,480)
    