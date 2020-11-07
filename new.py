def pattern(n):
    pyramid=2*n-2
    for i in range(n,-1,-1):
        for j in range (pyramid,0,-1):
            print(end="")
        pyramid=pyramid-1
        for j in range( 0, i+1):
            print("*", end="")
            
print(pattern(5))
