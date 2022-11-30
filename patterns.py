#qn1
"""n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()"""


#qn2
"""n=int(input())
for i in range(1,n+1):
    print(str(i)*i)"""


#qn3
"""n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for _ in range(i):
        print(i,end="")
        i-=1
    print()
print()"""


#qn3v2
"""n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()"""


#qn4
"""n=int(input())
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=' ')
    print()"""



#qn5
"""n=int(input())
for i in range(n+1):
    print(" "*(i),end="")
    for j in range(1,n-i+1):
        print(j,end="")
    print()"""



#qn6
"""n=int(input())
j=1
for i in range(1,n+1):
    k=1
    while k<=i:
        print(j,end=" ")
        j+=1
        k+=1
    print()"""



#qn7
"""n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))"""



#pascals
"""n=int(input())
n+=1
for i in range(1,n+1):
    c=1
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(c,end=" ")
        c=int(c*(i-j)/j)
    print()"""



#pyramid
"""n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for _ in range(1,i+1):
        print(0,end=" ")
    print()"""
