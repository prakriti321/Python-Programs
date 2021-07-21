no=int(input("Enter number of rows: "))
bool=input("Enter 1 for Upright Pattern, 0 for Downside Pattern: ")
i,j=0,0
j1=0

if bool == "1":
    for i in range(no):
        for j in range(no):
            if j <= i:
                print(" * ",end="")
        print("\n")
else:
    n=no
    while n != 0:
        for j1 in range(no):
            if j1 < n:
                print(" * ",end="")
        n -= 1
        print("\n")



