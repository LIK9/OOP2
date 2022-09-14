a = 1.614124
b = 4.123123

def f(x):
    return x**2 - x -1

limit = 0.00000001

while True:
    m  = (a + b) / 2.0
    
    if abs(f(m)) < limit and abs((b-a)/2) < limit:
        break
    
    else:
        if (f(a) * f(m)) < 0:
            b = m
        else:
            a = m
            
    print(m)
    
