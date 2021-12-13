M,N =input().split()
M=int(M)
N=int(N)

# Function
def Row_print(X,Y):
    n = Y - 1
    t = 0
    for i in range(1, (n + Y) + 1) :
        t = t + 1
    t1=t*3
    p=(X-t1)/2
    for j in range(1,(X-t1)+2):
        if j == p+1:
            for i in range(1,(n + Y)+1) :
                print(".|.", end="")
        else:
            print("-",end="")
    print()

def Welcome(X):
    a = X-7
    for i in range(1,a+2):
        if i == ((a/2)+1):
            print("WELCOME",end="")
        else:
            print("-",end="")
    print()

# MAIN .....
M1=int((M-1)/2)

for num1 in range(1,(M1+1)):
    Row_print(N,num1)
Welcome(N)
for num2 in reversed(range((M1+1))):
    if num2==0:
        pass
    else:
        Row_print(N,num2)
print(orktork)
