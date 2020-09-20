num = 4
k = 2 * num - 2
for i in range(0,num):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print(j+1, end=" ")
    print(" ")
    
