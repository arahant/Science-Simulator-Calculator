import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateTime(iVy,g):
    return float(iVy)/g

def calculateRange(time,iVx):
    return float(iVx)*time

def calculateHeight(iVy,g):
    return float(math.pow(iVy,2))/(2*g)

def getY_X_TrajectoryEquation(x,iVx,g,angle):
    return nm.tan(nm.pi*angle/180)*x - float(g)/(2*iVx*iVx)*(x*x)

def getY_Time_TrajectoryEquation(iVy,g,t):
    return float(iVy)*t - float(g)/2*(t*t)

def getVy_Time_Equation(iVy,g,t):
    return float(iVy) - float(g)*t

#
def initiate():
    g = 9.86
    angle = input("Enter the initial projectile angle: ")
    iVelocity = input("Enter the initial projectile velocity: ")
    calculate(g,angle,iVelocity)

def calculate(g,angle,iVelocity):
    iVx = float(iVelocity)*nm.cos(nm.pi*float(angle)/180)
    print("Initial velocity along x axis is "+str(iVx)+" m/s")
    iVy = float(iVelocity)*nm.sin(nm.pi*float(angle)/180)
    print("Initial velocity along y axis is "+str(iVy)+" m/s")
    time = calculateTime(iVy,g)
    print("The projectile duration is "+str(time*2)+" s")
    range = calculateRange(time*2,iVx)
    print("The max. projectile range is "+str(range)+" m")
    height = calculateHeight(iVy,g)
    print("The max. projectile height is "+str(height)+" m")
    plot_graphs(g,angle,iVelocity,iVx,iVy,time,range)

def plot_graphs(g,angle,iV,iVx,iVy,time,range):
    t = nm.arange(0,2*time,float(time)/10)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(t,getY_Time_TrajectoryEquation(iVy,g,t),'r--')
    plt.title("Projectile motion - Height Trajectory(t)")

    plt.subplot(212)
    plt.plot(t,getVy_Time_Equation(iVy,g,t),'r--')
    plt.title("Projectile motion - Vy(t)")

    x = nm.arange(0,range,0.1)
    plt.figure(2)
    plt.subplot(111)
    plt.plot(x,getY_X_TrajectoryEquation(x,iVx,g,angle),'r--')
    plt.title("Projectile motion - Height Trajectory(x)")

    plt.show()

#
initiate()
