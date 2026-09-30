import numpy as np

def trapezoidalQuad(f, a, b, dx):
    N = int((b-a)/dx) + 1
    w = np.full(N, 1.0)
    w[0] = w[N- 1] = 0.5
    x = np.linspace(a, b, len(w)) # Ensures that w and x have same length
    dx = x[1]- x[0] # Handles rounding weirdness
    y = w*f(x)
    return np.sum(y)*dx # Multiply here to avoid subtractive cancellation

def f(x):
    return (x- 2.0)**3- 3.5*x + 8.0

print(trapezoidalQuad(f, 0, 4, 0.1))
