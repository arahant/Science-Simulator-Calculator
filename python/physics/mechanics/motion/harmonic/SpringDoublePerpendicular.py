import math
import numpy as nm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def calculateKx(x,y,K1,K2,A,B):
    theta1 = nm.arctan(float(x)/(y+A))
    theta2 = nm.arctan(float(y)/(x+B))
    Kx = nm.abs(K2*nm.cos(theta2)) + nm.abs(K1*nm.sin(theta1))
    return Kx

def calculateKy(x,y,K1,K2,A,B):
    theta1 = nm.arctan(float(x)/(y+A))
    theta2 = nm.arctan(float(y)/(x+B))
    Ky = nm.abs(K2*nm.sin(theta2)) + nm.abs(K1*nm.cos(theta1))
    return Ky

def calculateOscillationTime(mass,K):
    return math.sqrt(float(mass)/K)*2*nm.pi

def calculatePotentialEnergy(K,d):
    return float(K)*d*d/2

def calculateKineticEnergy(K,D,d):
    KE = calculatePotentialEnergy(K,D) \
        - calculatePotentialEnergy(K,d)
    return KE

def calculateVelocity(mass,K,D,d, KE=0):
    if KE <= 0:
        velocity = math.sqrt(float(K)*(D*D - d*d)/mass)
    else:
        velocity = math.sqrt(float(KE)*2/mass)
    return velocity

def calculateResultantValue(v1,v2):
    return math.sqrt(float(v1)*v1+float(v2)*v2)

#
def getTrajectory_X(x,A,B):
    return float(A)*nm.sqrt(1 - x*x/(B*B))

def getTrajectory_Y(y,A,B):
    return float(B)*nm.sqrt(1 - y*y/(A*A))

def getPE_X_Equation(x,A,B,K1,K2):
    y = getTrajectory_X(x,A,B)
    theta1 = nm.arctan(x/(y+A))
    theta2 = nm.arctan(y/(x+B))
    Kx = nm.abs(K2*nm.cos(theta2)) + nm.abs(K1*nm.sin(theta1))
    return Kx*x*x/2

def getPE_Y_Equation(y,A,B,K1,K2):
    x = getTrajectory_Y(y,A,B)
    theta1 = nm.arctan(x/(y+A))
    theta2 = nm.arctan(y/(x+B))
    Ky = nm.abs(K2*nm.sin(theta2)) + nm.abs(K1*nm.cos(theta1))
    return Ky*y*y/2

def getPE_XY_Equation(x,y,A,B,K1,K2):
    theta1 = nm.arctan(x/(y+A))
    theta2 = nm.arctan(y/(x+B))
    Kx = nm.abs(K2*nm.cos(theta2)) + nm.abs(K1*nm.sin(theta1))
    Ky = nm.abs(K2*nm.sin(theta2)) + nm.abs(K1*nm.cos(theta1))
    return Kx*x*x/2 + Ky*y*y/2

#
def initiate():
    mass = input("Enter the mass of the object: ")
    K1 = input("The vertical spring A constant: ")
    A = input("The max y-displacement of spring A: ")
    K2 = input("The horizontal spring B constant: ")
    B = input("The max x-displacement of spring B: ")
    calculate(mass,K1,A,K2,B)

def calculate(mass,K1,A,K2,B):
    y = input("Enter the initial y-displacement: ")
    x = input("Enter the initial x-displacement: ")
    Kx = calculateKx(x,y,K1,K2,A,B)
    Ky = calculateKy(x,y,K1,K2,A,B)
    K = calculateResultantValue(Kx,Ky)

    time = calculateOscillationTime(mass,K)
    print("The oscillation time is "+str(time)+" s")

    Kx_max = calculateKx(B,0,K1,K2,A,B)
    PEx_max = calculatePotentialEnergy(Kx_max,B)
    print("The max PEx at ("+str(B)+",0) is "+str(PEx_max)+" Nm")
    Ky_max = calculateKy(0,A,K1,K2,A,B)
    PEy_max = calculatePotentialEnergy(Ky_max,A)
    print("The max PEy at (0,"+str(A)+") is "+str(PEy_max)+" Nm")

    PEx = calculatePotentialEnergy(Kx,x)
    print("The initial PE-x is "+str(PEx)+" Nm")
    PEy = calculatePotentialEnergy(Ky,y)
    print("The initial PE-y is "+str(PEy)+" Nm")
    PE = calculateResultantValue(PEx,PEy)
    print("The initial PE is "+str(PE)+" Nm")

    #d = x*nm.cos(theta) + y*nm.sin(theta)
    #vel = calculateVelocity(mass,K,D,d,KE)
    #print("The velocity at ("+str(x)+","+str(y)+") is "+str(vel)+" m/s")

    plot_graphs(mass,K1,A,K2,B)

def plot_graphs(mass,K1,A,K2,B):
    x = nm.arange(0,B-0.01,float(B)/100)
    #y1 = getTrajectory_X(x,A,B)
    y = nm.arange(0,A-0.01,float(A)/100)

    plt.figure(1)
    plt.subplot(211)
    Tx = getTrajectory_X(x,A,B)
    plt.plot(x,Tx)
    plt.title("Trajectory(x)")
    plt.subplot(212)
    Ty = getTrajectory_Y(y,A,B)
    plt.plot(y,Ty)
    plt.title("Trajectory(y)")

    plt.figure(2)
    plt.subplot(211)
    PEx = getPE_X_Equation(x,A,B,K1,K2)
    plt.plot(x,PEx,'r--')
    plt.title("PE(x)")
    plt.subplot(212)
    PEy = getPE_Y_Equation(y,A,B,K1,K2)
    plt.plot(y,PEy,'r--')
    plt.title("PE(y)")

    fig3 = plt.figure(3)
    ax3D = fig3.gca(projection='3d')
    ax3D.grid(True)
    ax3D.set_xlabel("X-axis")
    ax3D.set_ylabel('Y-axis')
    ax3D.set_zlabel('Resultant PE')
    #ax3D.set_ylim3d(bottom=0,top=Tx.all())
    x,y = nm.meshgrid(x,Tx)
    PExy = getPE_XY_Equation(x,y,A,B,K1,K2)
    surf = ax3D.plot_surface(x,y,PExy,cmap=cm.coolwarm,linewidth=0, antialiased=False)
    fig3.colorbar(surf, shrink=0.5, aspect=5)
    plt.title("PE(x,y)")

    plt.show()

#
initiate()
