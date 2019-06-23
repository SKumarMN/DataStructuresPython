def subArrayExists( arr, n):
    s = set()
    sum = 0

    for i in range(n):

        sum +=arr[i]

        if(sum == 0 or sum in s):
            return True
        else:
            s.add(sum)





arr2=[4, 2, -3, 1, 6]
arr = [-3, 2, 3, 1, 6] 
n = len(arr2) 
if subArrayExists(arr2, n) == True: 
    print("Found a sunbarray with 0 sum") 
else: 
    print("No Such sub array exits!")