def pair_sum(input, sum):

    map= {}
    for element in input:
        diff=  sum - element

        if( diff in map):
            print( diff, element)
        else:
            map[element] = element


l= [ 2, 3, 4, -2, 6, 8, 9, 11,0 ]; 

pair_sum(l,6)

