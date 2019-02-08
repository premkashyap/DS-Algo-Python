def heapPermutation(a, size):
    print(a, size)
    if size == 1:
        print(a)
        return
    for i in range(size):
        heapPermutation(a,size-1)
        print(a, size, i)
        if (size%2==1):
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]

# Program to print all combination  
# of size r in an array of size n 
  
 
# arr[] ---> Input Array 
# data[] ---> Temporary array to 
#         store current combination 
# start & end ---> Staring and Ending 
#             indexes in arr[] 
# index ---> Current index in data[] 
# r ---> Size of a combination  
# to be printed  
def combinationUtil(arr, data, start,  
                    end, index, r): 
                          
    # Current combination is ready  
    # to be printed, print it 
    if (index == r): 
        print(data, end = " ")
        print() 
        return
  
    # replace index with all 
    # possible elements. The 
    # condition "end-i+1 >=  
    # r-index" makes sure that  
    # including one element at 
    # index will make a combination  
    # with remaining elements at  
    # remaining positions 
    i = start  
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i] 
        combinationUtil(arr, data, i + 1,  
                        end, index + 1, r) 
        i += 1
     

if __name__ == '__main__':
    a = [1, 2, 3, 4,5] 
    n = len(a)
    #heapPermutation(a, n) 
    r = 3
    data = [0]*r
    combinationUtil(a, data, 0,  
                    n-1, 0, r)