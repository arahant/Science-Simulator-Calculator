import math
import numpy as nm
import matplotlib.pyplot as plt

def calculateOscillationTime(mass,K):
    return math.sqrt(float(mass)/K)*2*nm.pi

def calculatePotentialEnergy(K,x):
    return float(K)*x*x/2

def calculateKineticEnergy(K,A,x):
    KE = calculatePotentialEnergy(K,A) \
        - calculatePotentialEnergy(K,x)
    return KE

def calculateVelocity(mass,K,A,x, KE=0):
    if KE <= 0:
        velocity = math.sqrt(float(K)*(A*A - x*x)/mass)
    else:
        velocity = math.sqrt(float(KE)*2/mass)
    return velocity

def getPE_Distance_Equation(x,K):
    return float(K)*x*x/2

def getKE_Distance_Equation(A,x,K):
    return float(K)*A*A/2 - float(K)*x*x/2

def initiate():
    mass = input("Enter the mass of the object: ")
    A1 = input("Enter the 1st spring's initial displacement: ")
    K1 = input("Enter the 1st spring constant: ")
    A2 = input("Enter the 2nd spring's initial displacement: ")
    K2 = input("Enter the 2nd spring constant: ")
    type = input("Choose serial or parallel: ")
    #K = type.lower().contains('parallel')?(float(K1)*K2/(K1 + K2)):(K1+K2)
    K=K1+K2
    if type.lower().find('parallel') >= 0:
        K = float(K1)*K2/(K1 + K2)
    A = A1+A2
    if type.lower().find('parallel') >= 0:
        A = float(A1)*A2/(A1 + A2)
    calculate(mass,A,K)

def calculate(mass,A,K):
    print("Resultant K is "+str(K))
    time = calculateOscillationTime(mass,K)
    print("The total oscillation time is "+str(time)+" s")
    PE = calculatePotentialEnergy(K,A)
    print("The initial PE is "+str(PE)+" Nm")

    x = input("Enter the displacement at which PE, KE, Velocity needs to be determined: ")
    PE = calculatePotentialEnergy(K,x)
    print("The PE at "+str(x)+"m is "+str(PE)+" Nm")
    KE = calculateKineticEnergy(K,A,x)
    print("The KE at "+str(x)+"m is "+str(KE)+" Nm")
    vel = calculateVelocity(mass,K,A,x,KE)
    print("The velocity at "+str(x)+"m is "+str(vel)+" m/s")

    plot_graphs(A,K,mass)

def plot_graphs(A,K,mass):
    ax = nm.arange(-A,A,float(A)/10)
    plt.figure(1)
    plt.subplot(111)
    plt.plot(ax,getPE_Distance_Equation(ax,K),'r--')
    plt.plot(ax,getKE_Distance_Equation(A,ax,K),'r--')
    plt.title("PE vs KE")
    plt.show()

#
initiate()
