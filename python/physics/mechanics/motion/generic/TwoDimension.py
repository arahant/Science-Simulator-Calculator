import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateAcceleration(V1,V2,t):
    return float(V2-V1)/t

def calculateDistance(V1,V2,t,acc=0):
    if acc == 0:
        acc = calculateAcceleration(V1,V2,t)
    return float(V1)*t + float(acc)*t*t/2

def calculateForce(mass,V1,V2,t,acc=0):
    if acc == 0:
        acc = calculateAcceleration(V1,V2,t)
    return mass*acc

def calculateResultantValue(V1,V2):
	return math.sqrt(float(V1)*V2+float(V2)*V2);

def getDistanceEquation(t, V, acc):
    return float(V)*t + float(acc)*(t*t)/2

#
def initiate():
    mass = input("Enter the mass of the object: ")
    V1 = input("Enter the initial velocity of the object: ")
    angle1 = input("Enter the initial angle with x-axis: ")
    V2 = input("Enter the current velocity of the object: ")
    angle2 = input("Enter the current angle with x-axis: ")
    t = input("Enter the duration of motion: ")
    calculate(mass,V1,angle1,V2,angle2,t)

def calculate(mass,V1,angle1,V2,angle2,t):
    V1X = float(V1)*nm.cos(nm.pi*angle1/180)
    V1Y = float(V1)*nm.sin(nm.pi*angle1/180)
    V2X = float(V2)*nm.cos(nm.pi*angle2/180)
    V2Y = float(V2)*nm.sin(nm.pi*angle2/180)

    accX = calculateAcceleration(V1X,V2X,t)
    print("Acceleration-x is "+str(accX)+" m/s2")
    accY = calculateAcceleration(V1Y,V2Y,t)
    print("Acceleration-y is "+str(accY)+" m/s2")
    acc = calculateResultantValue(accX,accY)
    print("Resultant acceleration is "+str(acc)+" m/s2")

    distanceX = calculateDistance(V1X,V2X,t,accX)
    print("X Distance travelled is "+str(distanceX)+" m")
    distanceY = calculateDistance(V1Y,V2Y,t,accY)
    print("Y Distance travelled is "+str(distanceY)+" m")
    distance = calculateResultantValue(distanceX,distanceY)
    print("Resultant distance = "+str(distance)+" m")

    forceX = calculateForce(mass,V1X,V2X,t,accX)
    print("Internal x-force is "+str(forceX)+" N")
    forceY = calculateForce(mass,V1Y,V2Y,t,accY)
    print("Internal y-force is "+str(forceY)+" N")
    force = calculateResultantValue(forceX,forceY)
    print("Resultant internal force is "+str(force)+" N")

    plot_graphs(V1X,V1Y,accX,accY)

def plot_graphs(V1X,V1Y,accX,accY):
    t = nm.arange(0.0,10.0,0.5)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(t,getDistanceEquation(t,V1X,accX),'r--')
    plt.title("DistanceX(t)")

    plt.subplot(212)
    plt.plot(t,getDistanceEquation(t,V1Y,accY),'r--')
    plt.title("DistanceY(t)")
    plt.show()

#
initiate()
