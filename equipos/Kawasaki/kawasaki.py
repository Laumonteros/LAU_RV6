#RobotName: Kawasaki
from RobotRL import RobotRL

robot = RobotRL()

di = 0
dd = 0
variable = 0

def Velocidade():
    robot.setVD(100)
    robot.setVI(100)

def atrasss():
    robot.setVD(-70)
    robot.setVI(-70)

def girar_d():
    robot.setVI(60)
    robot.setVD(60)

def derecha():
    robot.setVI(60)
    robot.setVD(-60)

def noCaer():
    if (robot.getColorPiso() > 90):
        atrasss()
        robot.esperar(2)
        izquierda()
        robot.esperar(1)
    else:
        buscar1()

def izquierda():
    robot.setVI(-60)
    robot.setVD(60)

def buscar1():
    global di, dd, variable
    di = robot.getDI()
    dd = robot.getDD()
    if ((di <= 80) and (dd <= 80)):
        variable = 1
        Velocidade()
    if ((di > 80) and (dd < 80)):
        derecha()
        variable = 1
    if ((di < 80) and (dd > 80)):
        izquierda()
        variable = 1
    if (variable != 1):
        girarl()
    print(di)
    print(dd)

def girarl():
    robot.setVI(-50)
    robot.setVD(50)

while robot.step():
    noCaer()

