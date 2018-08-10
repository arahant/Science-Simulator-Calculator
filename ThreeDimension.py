import math
import numpy as nm
import matplotlib.pyplot as plt

# along x-axis
def calculateAccelerationX(v2, t):
    accX = (v2 - iVelocityX)/t
    return accX

def calculateDistanceX(v2, t):
    if accX == 0:
        calculateAccelerationX(v2,t)
    distanceX = iVelocityX*t + accX*t*t/2
    return distanceX

def calculateForceX(v2, t):
    if accX == 0:
        calculateAccelerationX(v2,t)
    forceX = mass*accX
    return forceX

def getDistanceEquationX(t, iVelocityX, accX):
    return iVelocityX*t + float(accX)/2*(t*t)

# along y-axis
def calculateAccelerationY(v2, t):
    accY = (v2 - iVelocityY)/t
    return accY

def calculateDistanceY(v2, t):
    if accY == 0:
        calculateAccelerationY(v2,t)
    distanceY = iVelocityY*t + accY*t*t/2
    return distanceY

def calculateForceY(v2, t):
    if accY == 0:
        calculateAccelerationY(v2,t)
    forceY = mass*accY
    return forceY

def getDistanceEquationY(t, iVelocityY, accY):
    return iVelocityY*t + float(accY)/2*(t*t)

# along z-axis
def calculateAccelerationZ(v2, t):
    accZ = (v2 - iVelocityZ)/t
    return accZ

def calculateDistanceZ(v2, t):
    if accZ == 0:
        calculateAccelerationZ(v2,t)
    distanceZ = iVelocityZ*t + accZ*t*t/2
    return distanceZ

def calculateForceZ(v2, t):
    if accZ == 0:
        calculateAccelerationZ(v2,t)
    forceZ = mass*accZ
    return forceZ

def getDistanceEquationZ(t, iVelocityZ, accZ):
    return iVelocityZ*t + float(accZ)/2*(t*t)

# final
def calculateAcceleration():
	return math.sqrt(math.pow(accX,2)+math.pow(accY,2)+math.pow(accZ,2));

def calculateDistance():
	return math.sqrt(math.pow(distanceX,2)+math.pow(distanceY,2)+math.pow(distanceZ,2));

def calculateForce():
	return math.sqrt(math.pow(forceX,2)+math.pow(forceY,2)+math.pow(forceZ,2));

#
accX = 0
accY = 0
accZ = 0
acc = 0
distanceX = 0
distanceY = 0
distanceZ = 0
distance = 0
forceX = 0
forceY = 0
forceZ = 0
force = 0

mass = input("Enter the mass of the object: ")
iVelocityX = input("Enter the initial x-velocity of the object: ")
iVelocityY = input("Enter the initial y-velocity of the object: ")
iVelocityZ = input("Enter the initial z-velocity of the object: ")
v2X = input("Enter the current x-velocity of the object: ")
v2Y = input("Enter the current y-velocity of the object: ")
v2Z = input("Enter the current z-velocity of the object: ")
t = input("Enter the duration of motion: ")

accX = calculateAccelerationX(v2X,t)
print("Acceleration-x is "+str(accX)+" m/s2")
accY = calculateAccelerationY(v2Y,t)
print("Acceleration-y is "+str(accY)+" m/s2")
accZ = calculateAccelerationZ(v2Z,t)
print("Acceleration-z is "+str(accZ)+" m/s2")
acc = calculateAcceleration()
print("Resultant acceleration is "+str(acc)+" m/s2")

distanceX = calculateDistanceX(v2X,t)
print("X Distance travelled is "+str(distanceX)+" m")
distanceY = calculateDistanceY(v2Y,t)
print("Y Distance travelled is "+str(distanceY)+" m")
distanceZ = calculateDistanceZ(v2Z,t)
print("Z Distance travelled is "+str(distanceZ)+" m")
distance = calculateDistance()
print("Resultant distance = "+str(distance)+" m")

forceX = calculateForceX(v2X,t)
print("Internal force-x is "+str(forceX)+" N")
forceY = calculateForceY(v2Y,t)
print("Internal force-y is "+str(forceY)+" N")
forceZ = calculateForceZ(v2Z,t)
print("Internal force-Z is "+str(forceZ)+" N")
force = calculateForce()
print("Resultant internal force is "+str(force)+" N")

t1 = nm.arange(-10.0,10.0,0.5)
plt.figure(1)
plt.subplot(311)
plt.plot(t1,getDistanceEquationX(t1, iVelocityX, accX),'r--')
plt.legend("X axis")

plt.subplot(312)
plt.plot(t1,getDistanceEquationY(t1, iVelocityY, accY),'r--')
plt.legend("Y axis")

plt.subplot(313)
plt.plot(t1,getDistanceEquationZ(t1, iVelocityZ, accZ),'r--')
plt.legend("Z axis")
plt.show()
