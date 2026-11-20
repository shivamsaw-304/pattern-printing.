# * * * * *
# * * * *
# * * *
# * *
# *


n = int(input("Enter number :"))

for i in range(n ,0,-1): # just reversing the traversal of loop 
    for j in range(i):# same inner loop is depended on 
        print("*", end=" ")
    print()