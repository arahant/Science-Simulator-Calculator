import numpy as nm
import matplotlib.pyplot as plt

def calculateAcceleration(iVelocity,v2,t):
    return float(v2-iVelocity)/t

def calculateDistance(iVelocity,v2,t,acc=0):
    if acc == 0:
        acc = calculateAcceleration(iVelocity,v2,t)
    return float(iVelocity)*t + float(acc)*t*t/2

def calculateForce(mass,iVelocity,v2,t,acc=0):
    if acc == 0:
        acc = calculateAcceleration(iVelocity,v2,t)
    return mass*acc

def getDistanceEquation(t, iVelocity, acc=0):
    if acc == 0:
        acc = calculateAcceleration(iVelocity,v2,t)
    return float(iVelocity)*t + float(acc)*(t*t)/2

#
def initiate():
    mass = input("Enter the mass of the object: ")
    iVelocity = input("Enter the initial velocity of the object: ")
    v2 = input("Enter the current velocity of the object: ")
    t = input("Enter the duration of motion: ")
    calculate(mass,iVelocity,v2,t)

def calculate(mass,iVelocity,v2,t):
    acc = calculateAcceleration(iVelocity,v2,t)
    print("Acceleration is "+str(acc)+" m/s2")
    distance = calculateDistance(iVelocity,v2,t,acc)
    print("Distance travelled is "+str(distance)+" m")
    force = calculateForce(mass,iVelocity,v2,t,acc)
    print("Internal force is "+str(force)+" N")
    plot_graphs(mass,iVelocity,v2,t,acc)

def plot_graphs(mass,iVelocity,v2,t,acc):
    t = nm.arange(0.0,10.0,0.1)
    plt.figure(1)
    plt.subplot(111)
    plt.plot(t,getDistanceEquation(t, iVelocity, acc),'r--')
    plt.show()

#
initiate()
