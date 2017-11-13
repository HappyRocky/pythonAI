def factorial(n):
    if isinstance(n,int) and n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        return None
    
for x in range(10):
    print("{}!={}".format(x,factorial(x)))
            
        
        