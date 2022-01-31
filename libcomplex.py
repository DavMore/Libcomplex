
from math import *

def sumacplx(a,b):
    real=a[0]+b[0]
    img=a[1]+b[1]
    return  (real, img)


def multcplx(a,b):
    real=(a[0]*b[0])-(a[1]*b[1])
    img=(a[0]*b[1])+(b[0]*a[1])
    return(real, img)

def prettyprinting(c):
    print (str(c[0])+ "+" + str(c[1])+ "i")

def divcplx(a,b):
    x=(a[0]*b[0]+a[1]*b[1])/((b[0]**2+b[1]*2))
    y=(b[0]*a[1]-a[0]*b[1])/((b[0]**2+b[1]*2))
    return (x, y)


prettyprinting(sumacplx((2,3),(4,7)))
prettyprinting(multcplx((2,3),(4,7)))
prettyprinting(divcplx((-2, 1), (1, 2)))

def mod(c):
    sq = c[0]**2 + c[1]**2
    r = sqrt(sq)
    return (r)
print(mod((4, 3))
      
def conj(c):
    return(c[0], -c[1])


def phase(c):
    if c[0] == 0 and c[1] == 0:
        return 0
    if c[0] == 0 and c[1] > 0:
        return pi
    if c[0] ==0 and c[1] <0:
        return 3 * pi/2

theta = atan(c[1]/c[0])
if c[0]>0 and c[1]>=0:
    return theta
if c[0]<0 and c[1]>0:
    return abs(thetha) + pi/2
if c[0]<0 and c[1]<=0:
    return abs(theta) + pi
if c[0]>0 and c[1]<0:
    return abs(tetha) + 3 * pi/2

def rect_pol(c):
    rho = mod(c)
    phi=phase(c)
    return (rho, phi)

def pol_rect(c):
    real = c[0] * cos([1])
    img = c[0] * sin(([1])
    return (real, img)
