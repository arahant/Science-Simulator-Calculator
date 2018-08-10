import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateTime(iVy,g):
    time = float(iVy)/g
    return time

def calculateRange(time,iVx):
    range = float(iVx)*time
    return range

def calculateHeight(iVy,g):
    height = float(math.pow(iVy,2))/(2*g)
    return height

def getTrajectoryEquation(iVy,g,t):
    return float(iVy)*t - float(g)/2*(t*t)

def getVyEquation(iVy,g,t):
    return float(iVy) - float(g)*t

g = 9.86
angle = input("Enter the initial projectile angle: ")
iVelocity = input("Enter the initial projectile velocity: ")
iVx = float(iVelocity)*nm.cos(nm.pi*float(angle)/180)
print("Initial velocity along x axis is "+str(iVx)+" m/s")
iVy = float(iVelocity)*nm.sin(nm.pi*float(angle)/180)
print("Initial velocity along y axis is "+str(iVy)+" m/s")

time = calculateTime(iVy,g)
print("The projectile duration is "+str(time)+" s")
range = calculateRange(time,iVx)
print("The max. projectile range is "+str(range)+" m")
height = calculateHeight(iVy,g)
print("The max. projectile height is "+str(height)+" m")

t1 = nm.arange(0,2*time,0.1)
plt.figure(1)
plt.subplot(211)
plt.plot(t1,getTrajectoryEquation(iVy,g,t1),'r--')
plt.legend("P(t)")

plt.subplot(212)
plt.plot(t1,getVyEquation(iVy,g,t1),'r--')
plt.legend("Vy(t)")
plt.show()
