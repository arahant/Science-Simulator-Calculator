import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateOscillationTime(angle,radius,g):
    time = math.sqrt(float(radius)/g)*2*nm.pi
    return time

def calculatePotentialEnergy(a,g,radius,mass):
    PE = float(mass)*g*radius*(1-nm.cos(a))
    return PE

def calculateKineticEnergy(angle,a,g,radius,mass):
    KE = calculatePotentialEnergy(angle,g,radius,mass) - calculatePotentialEnergy(a,g,radius,mass)
    return KE

def calculateVelocity(a,g,radius, KE=0):
    if KE <= 0:
        velocity = math.sqrt(2*g*radius*(1-nm.cos(a)))
    else:
        velocity = math.sqrt(float(KE)*2/mass)
    return velocity

def getPEEquation(ax,mass,g,radius):
    return float(mass)*g*radius-float(mass)*g*radius*nm.cos(ax)

def getKEEquation(angle,ax,mass,g,radius):
    return float(mass)*g*radius*nm.cos(ax)-float(mass)*g*radius*nm.cos(angle)

g = 9.86
mass = input("Enter the mass of the object ")
angle = input("Enter the initial title angle ")
angle = float(angle)/180*nm.pi
radius = input("Enter the radius of the pendulum string ")

time = calculateOscillationTime(angle, radius, g)
print("The total oscillation time is "+str(time)+" s")
PE = calculatePotentialEnergy(angle,g,radius,mass)
print("The initial PE is "+str(PE)+" Nm")

a = input("Enter the angle at which PE, KE, Velocity needs to be determined: ")
a = float(a)/180*nm.pi
PE = calculatePotentialEnergy(a,g,radius,mass)
print("The PE at "+str(a)+" degrees is "+str(PE)+" Nm")
KE = calculateKineticEnergy(angle,a,g,radius,mass)
print("The KE at "+str(a)+" degrees is "+str(KE)+" Nm")
vel = calculateVelocity(a,g,radius,KE)
print("The velocity at "+str(a)+" is "+str(vel)+" m/s")

ax = nm.arange(-angle,angle,angle/10)
plt.figure(1)
plt.subplot(211)
plt.plot(ax,getPEEquation(ax, mass, g, radius),'r--')
plt.legend("PE")

plt.subplot(212)
plt.plot(ax,getKEEquation(angle, ax, mass, g, radius),'r--')
plt.legend("KE")
plt.show()
