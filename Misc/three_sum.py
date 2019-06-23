def find_sum_of_three_v1(arr, required_sum):
  for i in range(0, len(arr)-2):
    for j in range(i+1, len(arr)-1):
      for k in range(j+1, len(arr)):
        #i,j and k are indices to cater the scenario in which same array element is used to calculate the sum.
        
          sum = arr[i] + arr[j] + arr[k]
          if sum == required_sum:
            return True
  return False

def test():
  arr = [-25, -10, -7, -3, 2, 4, 8, 10]
  print(find_sum_of_three_v1(arr, -8)) 
  print(find_sum_of_three_v1(arr, -25))
  print(find_sum_of_three_v1(arr, 0))
  print(find_sum_of_three_v1(arr, -42))
  print(find_sum_of_three_v1(arr, 22))
  print(find_sum_of_three_v1(arr, -7))
  print(find_sum_of_three_v1(arr, -3)) 
  print(find_sum_of_three_v1(arr, 2)) 
  print(find_sum_of_three_v1(arr, 4)) 
  print(find_sum_of_three_v1(arr, 8))
  print(find_sum_of_three_v1(arr, 7)) 
  print(find_sum_of_three_v1(arr, 1))
  
test()