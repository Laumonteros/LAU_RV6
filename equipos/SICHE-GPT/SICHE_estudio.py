#RobotName: SICHE
from RobotRL import RobotRL

robot = RobotRL()

di = 0
dd = 0
izquierda = 0
derecha = 0

LIMITE_RIVAL = 100
BRILLO_BORDE = 85
TOLERANCIA = 8
VerRival = 0
UltimoLado = 1
Reversa = 0
GiroBorde = 0
LecturaPiso = 0
ConfirmarBorde = 0

def BUSQUEDA_LADO():
    global UltimoLado
    if (UltimoLado == 1):
        robot.setVD(-35)
        robot.setVI(35)
    else:
        robot.setVD(35)
        robot.setVI(-35)

def BUSCAR():
    global di, dd, izquierda, LIMITE_RIVAL, derecha, VerRival, UltimoLado, TOLERANCIA
    di = robot.getDI()
    dd = robot.getDD()
    izquierda = ((di >= 0) and (di < LIMITE_RIVAL))
    derecha = ((dd >= 0) and (dd < LIMITE_RIVAL))
    if ((izquierda == 0) and (derecha == 0)):
        VerRival = 0
        BUSQUEDA_LADO()
    else:
        if (VerRival == 0):
            VerRival = 1
            if (derecha and (izquierda == 0)):
                UltimoLado = 1
            else:
                if (izquierda and (derecha == 0)):
                    UltimoLado = -1
                else:
                    if (dd < di):
                        UltimoLado = 1
                    else:
                        UltimoLado = -1
            if (izquierda and derecha):
                robot.setVD(100)
                robot.setVI(100)
            else:
                if derecha:
                    robot.setVD(40)
                    robot.setVI(100)
                else:
                    robot.setVD(100)
                    robot.setVI(40)
        else:
            if ((di < 12) and (dd < 12)):
                robot.setVD(100)
                robot.setVI(100)
            else:
                if (izquierda and derecha):
                    if ((di < 10) and (dd < 10)):
                        robot.setVD(100)
                        robot.setVI(100)
                    else:
                        if (dd < (di - TOLERANCIA)):
                            UltimoLado = 1
                            robot.setVD(75)
                            robot.setVI(100)
                        else:
                            if (di < (dd - TOLERANCIA)):
                                UltimoLado = -1
                                robot.setVD(100)
                                robot.setVI(75)
                            else:
                                robot.setVD(100)
                                robot.setVI(100)
                else:
                    if derecha:
                        UltimoLado = 1
                        robot.setVD(40)
                        robot.setVI(100)
                    else:
                        UltimoLado = -1
                        robot.setVD(100)
                        robot.setVI(40)

while robot.step():
    LecturaPiso = robot.getColorPiso()
    if (LecturaPiso > 70):
        ConfirmarBorde = (ConfirmarBorde + 1)
    else:
        ConfirmarBorde = 0
    if ((LecturaPiso > BRILLO_BORDE) or (ConfirmarBorde >= 2)):
        VerRival = 0
        Reversa = 8
        GiroBorde = 10
        robot.setVD(-90)
        robot.setVI(-90)
    else:
        if (Reversa > 0):
            Reversa = (Reversa - 1)
            robot.setVD(-90)
            robot.setVI(-90)
        else:
            if (GiroBorde > 0):
                GiroBorde = (GiroBorde - 1)
                robot.setVD(60)
                robot.setVI(-60)
            else:
                if (((robot.getBI() and robot.getBD()) and (robot.getDI() >= 100)) and (robot.getDD() >= 100)):
                    VerRival = 0
                    robot.setVD(100)
                    robot.setVI(100)
                else:
                    if ((robot.getBI() and (robot.getDI() >= 100)) and (robot.getDD() >= 100)):
                        VerRival = 0
                        robot.setVD(100)
                        robot.setVI(100)
                    else:
                        if ((robot.getBD() and (robot.getDI() >= 100)) and (robot.getDD() >= 100)):
                            VerRival = 0
                            robot.setVD(100)
                            robot.setVI(100)
                        else:
                            BUSCAR()

