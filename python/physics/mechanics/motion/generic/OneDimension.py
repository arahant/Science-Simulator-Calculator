import numpy as nm
import matplotlib.pyplot as plt

#def initiate(m=0,iV=0):
    #mass = m
    #iVelocity = iV

def calculateAcceleration(v2, t):
    acc = (v2 - iVelocity)/t
    return acc

def calculateDistance(v2, t):
    if acc == 0:
        calculateAcceleration(v2,t)
    distance = iVelocity*t + acc*t*t/2
    return distance

def calculateForce(v2, t):
    if acc == 0:
        calculateAcceleration(v2,t)
    force = mass*acc
    return force

def getAccelerationEquation(t, iVelocity):
    return (10 - iVelocity)/t

def getDistanceEquation(t, iVelocity, acc):
    return iVelocity*t + float(acc)/2*(t*t)

#
mass = input("Enter the mass of the object: ")
iVelocity = input("Enter the initial velocity of the object: ")
v2 = input("Enter the current velocity of the object: ")
t = input("Enter the duration of motion: ")

acc = calculateAcceleration(v2,t)
print("Acceleration is "+str(acc)+" m/s2")
distance = calculateDistance(v2,t)
print("Distance travelled is "+str(distance)+" m")
force = calculateForce(v2,t)
print("Internal force is "+str(force)+" N")

t1 = nm.arange(0.0,10.0,0.5)
plt.figure(1)
plt.subplot(211)
plt.plot(t1,getDistanceEquation(t1, iVelocity, acc),'r--')

plt.subplot(212)
plt.plot(t1,getAccelerationEquation(t1, iVelocity),'r--')
plt.show()
