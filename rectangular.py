def rectangularQuad_left(f, a, b, dx):
    N = int((b-a)/dx)
    result = 0.0
    for i in range(0,N+1,1):
        x = a + i*dx
        result += f(x)*dx
    return result

def rectangularQuad_right(f, a, b, dx):
    N = int((b-a)/dx)
    result = 0.0
    for i in range(0,N,1):
        x = a + (i+1)*dx
        result += f(x)*dx
    return result

def rectangularQuad_center(f, a, b, dx):
    N = int((b-a)/dx)
    result = 0.0
    for i in range(0,N,1):
        x = a + dx/2 + i*dx
        result += f(x)*dx
    return result

def f(x):
    function = (x-2)**3 - 3.5*x + 8
    return function

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
dx = float(input("Enter increment: "))

print("The left-evaluated integral is", rectangularQuad_left(f,a,b,dx))
print("The right-evaluated integral is", rectangularQuad_right(f,a,b,dx))
print("The center-evaluated integral is", rectangularQuad_center(f,a,b,dx))