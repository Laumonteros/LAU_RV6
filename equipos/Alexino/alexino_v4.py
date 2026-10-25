#RobotName: Alexino
from RobotRL import RobotRL

robot = RobotRL()

dd = 0
di = 0
BD = 0
BI = 0

def GIRO_LOCO():
    robot.setVI(-100)
    robot.setVD(100)
    robot.esperar(500 / 1000)
    robot.setVI(100)
    robot.setVD(-100)
    robot.esperar(500 / 1000)

def giro_en_si():
    robot.setVI(-100)
    robot.setVD(100)

robot.setVI(-100)
robot.setVD(-100)
robot.esperar(500 / 1000)
print("HOLA SOY ALEX")

def reintegro():
    global dd, di
    dd = robot.getDD()
    di = robot.getDI()
    if ((di < 3) and (dd < 3)):
        print(str(DI()) + str(DI()))
        retroceder()
        robot.esperar(200 / 1000)
    else:
        if ((di < 4) and (dd >= 100)):
            print(str(DI()) + str(DI()))
            giro_der()
            robot.esperar(450 / 1000)
        else:
            if ((dd < 4) and (di >= 100)):
                print(str(DI()) + str(DI()))
                giro_izq()
                robot.esperar(450 / 1000)

def retroceder():
    robot.setVI(-100)
    robot.setVD(-100)

def culo_atras():
    robot.setVI(100)
    robot.setVD(0)

def parar():
    robot.setVI(0)
    robot.setVD(0)

def bumpers():
    global BD, BI
    BD = robot.getBD()
    BI = robot.getBI()
    if (BD and BI):
        print(str(BD) + str(BI))
        retroceder()
    else:
        giro_en_si()
        if (BD or BI):
            print(str(BD) + str(BI))
            retroceder()

def Avanzar():
    robot.setVI(100)
    robot.setVD(100)

def BRILLO():
    return robot.getColorPiso()

def DD():
    global dd
    return dd

def DI():
    global di
    return di

def nocaer():
    if (robot.getColorPiso() > 85):
        print(BRILLO())
        giro_en_si()
        robot.esperar(300 / 1000)
        avanzar()
        robot.esperar(700 / 1000)

def giro_der():
    robot.setVI(100)
    robot.setVD(-100)

def giro_izq():
    robot.setVI(-100)
    robot.setVD(100)

def avanzar():
    robot.setVI(100)
    robot.setVD(100)

while robot.step():
    nocaer()
    bumpers()
    reintegro()

