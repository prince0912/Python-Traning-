def Magical_square(n):
    magicalSquare = []
    for i in range (n):
        L=[]
        for j in range(n):
            L.append(0)
        magicalSquare.append(L)
        
        i = n//2  # integer division
        j = n-1

        num = n*n
        count = 1

    while(count <= num):
        if(i== -1 and j == n):
            j = n-2
            i = 0
        else:
            if (j==n):
                j=0
            if (i<0):
                i=n-1
        if(magicalSquare [i][j]!=0):
            j= j-2
            i= i+1
            continue 
        else:
            magicalSquare [i][j]=count
            count +=1
            
        i = i - 1
        j = j + 1

    for i in range(n):
        for j in range(n):
            print(magicalSquare [i][j], end=" ")
        print()


Magical_square(3)

      
        
            
        