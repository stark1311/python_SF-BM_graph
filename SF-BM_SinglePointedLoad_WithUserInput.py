import numpy as np
import matplotlib.pyplot as plt

P = int(input("Enter the value of the Load :"))
L = int (input ("Enter the length of the beam :"))
a = int(input ("Enter the distance ,where the load is to be applied : "))

R1 = P*(L-a)/L
R2 =P*a/L


l= np.linspace(0,L, 100 )

X=[]
SF =[]
M = []

for x in l :
    if x <= a :
        m = R1*x
        sf = R1
    elif x > a :
        m = (R1*x) -(P*(x-a))
        sf = R1 - P
         
    M.append(m)
    X.append(x)
    SF.append(sf)

plt.subplot(2,1,1)
plt.plot(X,SF)
plt.plot([0,L],[0,0])
plt.plot([0,0],[0,R1],[L,L],[0,-R2])
plt.title("Shear Force Diagram")
plt.xlabel("Length in m")
plt.ylabel("Shear Force in N")

plt.subplot(2,1,2)
plt.plot(X,M)
plt.plot([0,L],[L,0])
plt.title("Bending Moment Diagram")
plt.xlabel("Length in m")
plt.ylabel("Bending moment in Nm")


plt.show()
