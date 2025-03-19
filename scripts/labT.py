#0e  139.0699
t = 1.659 #109, 0.95
xil = 81.9997#109 0.025
xir = 139.7839#109 0.975
a =  14
s = 11
n = 110
az = a + s / 2

z = (a - az) * (n - 1) ** 0.5 / s
print(z)

azz = s * 3

zz = (n - 1) * s / azz
print(zz)


