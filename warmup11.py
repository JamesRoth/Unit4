#James Roth
#3/26/18
#warmup11.py - is a number prime

def prime(num):
    for i in range(2, num/2):
        if num%i==0:
            return "True"
            break
        
