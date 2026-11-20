# *
# * *
# * * *
# * * * *
# * * * * *

n = int(input("enter number :"))

for i in range(1,n+1): # for row traversing 

    for j in range(i): # inner loop is depended on i so it will travell till i range value
        print("*", end=" ")

    print()