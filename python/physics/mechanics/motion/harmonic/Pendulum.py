import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateOscillationTime(radius,g):
    return math.sqrt(float(radius)/g)*2*nm.pi

def calculatePotentialEnergy(a,g,radius,mass):
    a = getAngleInRadian(a)
    return float(mass)*g*radius*(1-nm.cos(a))

def calculateKineticEnergy(angle,a,g,radius,mass):
    KE = calculatePotentialEnergy(angle,g,radius,mass) \
        - calculatePotentialEnergy(a,g,radius,mass)
    return KE

def calculateVelocity(a,g,radius,mass, KE=0):
    a = getAngleInRadian(a)
    if KE <= 0:
        velocity = math.sqrt(2*g*radius*(1-nm.cos(a)))
    else:
        velocity = math.sqrt(float(KE)*2/mass)
    return velocity

def getAngleInRadian(angle):
    return float(angle)/180*nm.pi

def getPE_Angle_Equation(ax,mass,g,radius):
    return float(mass)*g*radius-float(mass)*g*radius*nm.cos(ax)

def getKE_Angle_Equation(angle,ax,mass,g,radius):
    return float(mass)*g*radius*nm.cos(ax)-float(mass)*g*radius*nm.cos(angle)

def initiate():
    g = 9.86
    mass = input("Enter the mass of the object ")
    angle = input("Enter the initial tilt angle ")
    radius = input("Enter the radius of the pendulum string ")
    calculate(g,mass,angle,radius)

def calculate(g,mass,angle,radius):
    time = calculateOscillationTime(radius, g)
    print("The total oscillation time is "+str(time)+" s")
    PE = calculatePotentialEnergy(angle,g,radius,mass)
    print("The initial PE is "+str(PE)+" Nm")

    a = input("Enter the angle at which PE, KE, Velocity needs to be determined: ")
    PE = calculatePotentialEnergy(a,g,radius,mass)
    print("The PE at "+str(a)+" degrees is "+str(PE)+" Nm")
    KE = calculateKineticEnergy(angle,a,g,radius,mass)
    print("The KE at "+str(a)+" degrees is "+str(KE)+" Nm")
    vel = calculateVelocity(a,g,radius,mass,KE)
    print("The velocity at "+str(a)+" is "+str(vel)+" m/s")

    plot_graphs(g,mass,angle,radius)

def plot_graphs(g,mass,angle,radius):
    b = getAngleInRadian(angle)
    ax = nm.arange(-b,b,b/10)
    plt.figure(1)
    plt.subplot(111)
    plt.plot(ax,getPE_Angle_Equation(ax, mass, g, radius),'r--',ax,getKE_Angle_Equation(b, ax, mass, g, radius),'r--')
    plt.title("PE vs KE")
    plt.show()

#
initiate()
