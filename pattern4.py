# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


n = int(input("enter number :"))

for i in range(1,n,1): # for row traversing 

    for j in range(1,i+1): # inner loop is depended on i so it will travell till i range value
        print(j, end=" ")

    print()