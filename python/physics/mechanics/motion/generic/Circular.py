import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateCentrifugalAcceleration():
    cfAcc = math.pow(velocity,2)/radius
    return cfAcc

def calculateCentrifugalForce():
	if cfAcc == 0:
		calculateCentrifugalAcceleration()
	cfForce = mass*cfAcc
	return cfForce

def calculateCentripetalForce():
	if cfForce == 0:
		calculateCentrifugalForce()
	cpForce = -cfForce
	return cpForce

def getDistanceEquation(theta):
	return float(radius)*nm.cos(theta)+float(radius)*nm.sin(theta)

#
mass = input("Enter the mass of the object: ")
radius = input("Enter the radius of the circular path: ")
velocity = input("Enter the constant velocity of the object: ")

cfAcc = calculateCentrifugalAcceleration()
print("The centrifugal acceleration is "+str(cfAcc)+" m/s2")
cfForce = calculateCentrifugalForce()
print("The centrifugal force is "+str(cfForce)+" N")
cpForce = calculateCentripetalForce()
print("The centripetal force is "+str(cpForce)+" N")

theta = nm.arange(-10*nm.pi,10*nm.pi,nm.pi/10)
plt.figure(1)
plt.subplot(111)
plt.plot(theta,getDistanceEquation(theta),'r--')
plt.legend("Circular")
plt.show()
