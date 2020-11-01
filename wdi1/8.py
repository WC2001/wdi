import time
start_time = time.time()
def pierwsza(x):

    if x==2  or x==3: 
        return True
    elif x<2 or x%2==0 or x%3==0: 
        return False
    
    i = 5
    while i*i <= x:
        if x%i==0: 
            return False
        i+=2
        if x%i==0: 
            return False
        i+=4

    return True


#x = int(input())
#print(pierwsza(x))
for i in range(0,100):
    pierwsza(i)

print(time.time() - start_time)