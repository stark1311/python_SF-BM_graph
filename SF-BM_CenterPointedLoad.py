import numpy as np
import matplotlib.pyplot as plt

P = int(input("Enter the value of the Load :"))
L = int (input ("Enter the length of the beam :"))


l= np.linspace(0,L, 100 )

X=[]
SF =[]
M = []

for x in l :
    if x <= L/2 :
        m = P * x
        sf = P
    elif x > L/2 :
        m = (P * L) - (P*x)
        sf = -P
         
    M.append(m)
    X.append(x)
    SF.append(sf)
        
plt.subplot(2,1,1)
plt.plot(X,M)
plt.plot([0,L],[L,0])
plt.title("Bending Moment Diagram")
plt.xlabel("Length in m")
plt.ylabel("Bending moment in Nm")


plt.subplot(2,1,2)
plt.plot(X,SF)
plt.plot([0,L],[0,0])
plt.plot([0,0],[0,P],[L,L],[0,-P])
plt.title("Shear Force Diagram")
plt.xlabel("Length in m")
plt.ylabel("Shear Force in N")


plt.show()

