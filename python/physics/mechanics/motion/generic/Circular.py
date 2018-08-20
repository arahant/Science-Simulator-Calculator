import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateCentrifugalAcceleration(velocity,radius):
    return math.pow(velocity,2)/radius

def calculateCentrifugalForce(mass,velocity,radius,cfAcc=0):
	if cfAcc == 0:
		cfAcc = calculateCentrifugalAcceleration(velocity,radius)
	return float(mass)*cfAcc

def calculateCentripetalForce(mass,velocity,radius,cfAcc=0):
	if cfAcc == 0:
		cfAcc = calculateCentrifugalAcceleration(velocity,radius)
	return -float(mass)*cfAcc

def getDisplacement_Angle_Equation(theta,radius):
	return float(radius)*nm.cos(theta)+float(radius)*nm.sin(theta)

def getDisplacement_X_Angle_Equation(theta,radius):
	return float(radius)*nm.cos(theta)

def getDisplacement_Y_Angle_Equation(theta,radius):
	return float(radius)*nm.sin(theta)

def getVelocity_X_Time_Equation(velocity,radius,phi,time):
    return float(velocity)*nm.cos(float(velocity)*time/radius+nm.pi*float(phi)/180)

def getVelocity_Y_Time_Equation(velocity,radius,phi,time):
    return float(velocity)*nm.sin(float(velocity)*time/radius+nm.pi*float(phi)/180)

#
def initiate():
    mass = input("Enter the mass of the object: ")
    radius = input("Enter the radius of the circular path: ")
    velocity = input("Enter the constant velocity of the object: ")
    phi = input("Enter the initial angle of the object with x axis: ")
    calculate(mass,radius,velocity,phi)

def calculate(mass,radius,velocity,phi):
    cfAcc = calculateCentrifugalAcceleration(velocity,radius)
    print("The centrifugal acceleration is "+str(cfAcc)+" m/s2")
    cfForce = calculateCentrifugalForce(mass,velocity,radius,cfAcc)
    print("The centrifugal force is "+str(cfForce)+" N")
    cpForce = calculateCentripetalForce(mass,velocity,radius,cfAcc)
    print("The centripetal force is "+str(cpForce)+" N")
    plot_graphs(mass,radius,velocity,phi)

def plot_graphs(mass,radius,velocity,phi):
    theta = nm.arange(nm.pi*(-1+float(phi)/180),nm.pi*(1+float(phi)/180),nm.pi/10)
    equation1 = getDisplacement_Angle_Equation(theta,radius)
    plt.figure(1)
    plt.subplot(311)
    plt.plot(theta,equation1,'r--')
    plt.title("Distance(@)")

    equation2 = getDisplacement_X_Angle_Equation(theta,radius)
    plt.subplot(312)
    plt.plot(theta,equation2,'r--')
    plt.title("DistanceX(@)")

    equation3 = getDisplacement_Y_Angle_Equation(theta,radius)
    plt.subplot(313)
    plt.plot(theta,equation3,'r--')
    plt.title("DistanceY(@)")

    time = nm.arange(0,10,0.1)
    equation4 = getVelocity_X_Time_Equation(velocity,radius,phi,time)
    plt.figure(2)
    plt.subplot(211)
    plt.plot(time,equation4)
    plt.title("VelocityX(t)")

    equation5 = getVelocity_Y_Time_Equation(velocity,radius,phi,time)
    plt.subplot(212)
    plt.plot(time,equation5)
    plt.title("VelocityY(t)")

    plt.show()

#
initiate()
