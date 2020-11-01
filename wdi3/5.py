n = int(input())

v = [0]*10

while n !=0:
        
        if n > v[9]:
            for i in range (0,10):
                
                if n > v[i]:
                    for j in range (0,9-i):
                        v[10-j-1] = v[10-j-2]
                    v[i] = n
                    break
        n = int(input()) 
print(v[9])


