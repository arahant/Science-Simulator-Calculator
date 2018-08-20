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
    return float(mass)*acc

def calculateResultantValue(V1,V2,V3):
	return math.sqrt(float(V1)*V2+float(V2)*V2+float(V3)*V3);

def getDistance_Time_Equation(t, V1, acc):
    return float(V1)*t + float(acc)*(t*t)/2

#
def initiate():
    mass = input("Enter the mass of the object: ")
    V1 = input("Enter the initial velocity of the object: ")
    phi1 = input("Enter the initial angle with z axis: ")
    theta1 = input("Enter the initial angle with x axis: ")
    V2 = input("Enter the current velocity of the object: ")
    phi2 = input("Enter the current angle with z axis: ")
    theta2 = input("Enter the current angle with x axis: ")
    t = input("Enter the duration of motion: ")
    calculate(mass,V1,phi1,theta1,V2,phi2,theta2,t)

def calculate(mass,V1,phi1,angle1,V2,phi2,angle2,t):
    V1XY = float(V1)*nm.sin(nm.pi*phi1/180)
    V1X = float(V1XY)*nm.cos(nm.pi*theta1/180)
    V1Y = float(V1XY)*nm.sin(nm.pi*theta1/180)
    V1Z = float(V1)*nm.cos(nm.pi*phi1/180)
    V2XY = float(V2)*nm.sin(nm.pi*phi2/180)
    V2X = float(V2XY)*nm.cos(nm.pi*theta2/180)
    V2Y = float(V2XY)*nm.sin(nm.pi*theta2/180)
    V2Z = float(V2)*nm.cos(nm.pi*phi2/180)

    accX = calculateAcceleration(V1X,V2X,t)
    print("Acceleration-x is "+str(accX)+" m/s2")
    accY = calculateAcceleration(V1Y,V2Y,t)
    print("Acceleration-y is "+str(accY)+" m/s2")
    accZ = calculateAcceleration(V1Z,V2Z,t)
    print("Acceleration-Z is "+str(accZ)+" m/s2")
    acc = calculateResultantValue(accX,accY,accZ)
    print("Resultant acceleration is "+str(acc)+" m/s2")

    distanceX = calculateDistance(V1X,V2X,t,accX)
    print("X Distance travelled is "+str(distanceX)+" m")
    distanceY = calculateDistance(V1Y,V2Y,t,accY)
    print("Y Distance travelled is "+str(distanceY)+" m")
    distanceZ = calculateDistance(V1Z,V2Z,t,accZ)
    print("Z Distance travelled is "+str(distanceZ)+" m")
    distance = calculateResultantValue(distanceX,distanceY,distanceZ)
    print("Resultant distance = "+str(distance)+" m")

    forceX = calculateForce(mass,V1X,V2X,t,accX)
    print("Internal force-x is "+str(forceX)+" N")
    forceY = calculateForce(mass,V1Y,V2Y,t,accY)
    print("Internal force-y is "+str(forceY)+" N")
    forceZ = calculateForce(mass,V1Z,V2Z,t,accZ)
    print("Internal force-z is "+str(forceZ)+" N")
    force = calculateResultantValue(forceX,forceY,forceZ)
    print("Resultant internal force is "+str(force)+" N")

    plot_graphs(V1X,V1Y,V1Z,accX,accY,accZ,t)

def plot_graphs(V1X,V1Y,V1Z,accX,accY,accZ,time):
    t = nm.arange(0,time*2,0.1)
    plt.figure(1)
    plt.subplot(311)
    plt.plot(t,getDistance_Time_Equation(t, V1X, accX),'r--')
    plt.title("DistanceX(t)")

    plt.subplot(312)
    plt.plot(t,getDistance_Time_Equation(t, V1Y, accY),'r--')
    plt.title("DistanceY(t)")

    plt.subplot(313)
    plt.plot(t,getDistance_Time_Equation(t, V1Z, accZ),'r--')
    plt.title("DistanceZ(t)")
    plt.show()

#
initiate()
