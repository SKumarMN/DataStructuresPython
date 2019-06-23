def selectionsort(input):

    n = len(input)

    for i in range(n):
        min = i

        for j in range( i+1, n ):
            if input[min] > input[j]:
                min = j
        input[i], input[min] = input[min], input[i]

    return input

def bubblesort(input):

    for i in range(len(input)):

        for j in range( 0, len(input)-i-1):
            if( input[j] > input[j+1]):
                input[j],input[j+1] = input[j+1], input[j]



def rec_bubblesort(input, n):

    if n == 1:
        return

    for j in range(n-1):
        if( input[j] > input[j+1]):
                input[j],input[j+1] = input[j+1], input[j]

    rec_bubblesort(input, n-1)


def insertionsort(input):

    for i in range(1, len(input)):

        key = input[i]

        j = i-1
        while(j >=0 and key < input[j]):
            input[j+1] = input[j]
            j-=1
        input[j+1] = key




def mergesort(arr):

    if len(arr)>1:
        mid = len(arr)//2
        L= arr[:mid]
        R= arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j= k =0

        while( i < len(L) and j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k]= R[j]
                j+=1
            k+=1

        
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

A = [64, 25, 12, 22, 11]
B = [11,12,13,14,15,16]
mergesort(A)



print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  
