#用公式解解一元二次方程式

a=1
b=2
c=-63

fenzi = -b + (b**2 - 4*a*c)**0.5
fenmu = 2*a

x = fenzi / fenmu

print(x) 

fenzi = -b - (b**2 - 4*a*c)**0.5
fenmu = 2*a

x = fenzi / fenmu

print(x)

