#James Roth
#3/29/18
#warmup12.py - returning GCF of 2 numbers

def gcf(num1,num2):
    MAXI=max(num1,num2)
    
    counter=min(num1,num2)
    
    while counter>0:
        if MAXI%counter==0 and min(num1,num2)%counter==0:
            ans=int(counter)
            print(int(counter))
            break
        else: 
            counter-=1

gcf(12,15)
gcf(9,5)
gcf(16,64)