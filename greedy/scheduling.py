def printMaxActivities(start, finish):

    i = 0
    print(start[i])

    for j in range(len(finish)):

        if start[j] >= finish[i]:
            print(start[j])
            i=j


def printMaxActivitiesSet(activity):
    newList = sorted(activity, key = lambda x: x[1])

    i = 0 
    print(newList[i][0])

    for j in range(len(newList)-1):
        j =j+1
        if newList[j][0] >= newList[i][1]:
            print(newList[j][0])
            i =j


start = [1,3,0,5,8,5]
finish= [2,4,6,7,9,9]

printMaxActivities(start,finish)
print("----")
activity = [(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
printMaxActivitiesSet(activity)
