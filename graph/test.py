
numVertices=3
val= [0]* numVertices
for i in range(numVertices):
            val[i]= [0]* numVertices

print(val)


def is_leap(year):
    leap = False
    print(year % 4)
    if(year % 4 == 0):
        if (year % 100 ==0 and year % 400 ==0):
            return True
        elif (year % 100 ==0 and year % 400 !=0):
            return False
        else:
            return True
    
    return leap

print(is_leap(1800))