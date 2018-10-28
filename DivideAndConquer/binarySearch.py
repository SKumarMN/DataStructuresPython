def binary_search(ilist,num ):
    if len(ilist) > 0:
        
        mid = len(ilist) // 2
        
        if ilist[mid] == num:
            return True
        elif num < ilist[mid]:           
            return binary_search(ilist[:mid],num)
        else:   
            return binary_search(ilist[mid+1:],num)
        
    else:
        return False


print(binary_search([1,4,8,10,24,56,73],70))

print(binary_search([1,4,8,10,24,56,73],0))

print(binary_search([1,4,8,10,24,56,73],73))