import turtle
import random

class Circuito():
    corredores = []
    __posStartY = [-30,-10,10,30]
    __colorTurtle = ['red','blue','green','orange']
    Ganador = None

    def __init__(self,width,height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgray')
        self.__startline = -width/2 + 20
        self.__finishline = height/2 + 40
        
        self.__createRunners()

    def __createRunners(self):
        for jugador in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape('turtle')
            new_turtle.color(self.__colorTurtle[jugador])
            new_turtle.setpos(self.__startline, self.__posStartY[jugador])
            #new_turtle.pendown()
            self.corredores.append(new_turtle)

    def competir(self):
        for jugador in self.corredores:
            if self.Ganador == None:
                avanza = random.randrange(1,6)
                if jugador.xcor() + avanza < self.__finishline:
                    jugador.fd(avanza)
                else:
                    self.Ganador = jugador.color()[0]
                    jugador.fd(self.__finishline - jugador.xcor())
                    print("La tortuga {} ha ganado.".format(self.Ganador))
                    
                



if __name__ == '__main__':
    circuito = Circuito(640,480)
    while circuito.Ganador == None:
        circuito.competir()
    