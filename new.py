def pattern(n):
    pyramid=2*n-2
    for i in range(0,n):
        for j in range(0, pyramid):
            print(end="")
        pyramid=pyramid-1
        for j in range( 0, i+1):
            print("*", end="")
        print("*")
            
print(pattern(9))
