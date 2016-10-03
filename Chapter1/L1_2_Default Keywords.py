def f(a,b, c=1, d=0 ,e=0):
    return (a+b)*c+d-e
    
    
print f(1,2)
# 3

print f(1,2,2)
# 6

print f(e=3,b=2,a=1)
# 0  

