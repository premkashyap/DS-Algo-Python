def factorial(n):
    #cache 
    cache = [0]*(n+1)
    #base condition
    cache[0] = cache[1]=1
    #function with closure 
    def _factorial(n, cache):
        #base conditions
        if cache[n] == 0:
            #recursive call
            cache[n] = n*_factorial(n-1, cache)
        return cache[n]
    return _factorial(n, cache)


def fibonacci(n):
    #cache
    cache = [None]*n

    #base condition
    cache[0]=0
    cache[1]=1

    def _fibonacci(n, cache):
        if cache[n-1] == None:
            #recursive call
            cache[n-1] = _fibonacci(n-1, cache) + _fibonacci(n-2, cache)
        return cache[n-1]

    _fibonacci(n, cache)
    return cache


def combination(total_no_of_object, no_of_object_to_select, is_order_important=False):
    #cache 
    cache = [0]*(total_no_of_object+1)
    #base condition
    cache[0] = cache[1] = 1

    def _factorial(n, cache):
        if cache[n] == 0:
            #recursive solution
            cache[n] = n*_factorial(n-1, cache)
        return cache[n]
    
    _factorial(total_no_of_object, cache)

    if is_order_important:
        return cache[total_no_of_object]/cache[no_of_object_to_select] 
    else:
        return cache[total_no_of_object]/(cache[no_of_object_to_select]*cache[total_no_of_object- no_of_object_to_select])


def number_of_subset_adding_to_a_number(arr, total):
    #cache
    cache = {}

    def _subset_adding_to_a_number(arr, total, i, cache):
        key = str(total) +':'+str(i)
        try:
            return cache[key]
        except KeyError:
            #base conditions
            if total == 0:
                return 1
            if total < 0:
                return 0
            if i < 0:
                return 0
            if arr[i] > total:
                return_val= _subset_adding_to_a_number(arr, total, i-1, cache)
            else:
                return_val= _subset_adding_to_a_number(arr, total, i-1, cache) + _subset_adding_to_a_number(arr, total-arr[i], i-1, cache)
            cache[key] = return_val
            return return_val

    return _subset_adding_to_a_number(arr, total, len(arr)-1, cache)


def number_of_subset_adding_to_a_number_repeation_allowed(arr, total):
    #cache
    cache = {}

    def _subset_adding_to_a_number(arr, total, i, cache):
        key = str(total) +':'+str(i)
        try:
            return cache[key]
        except KeyError:
            #base conditions
            if total == 0:
                return 1
            if total < 0:
                return 0
            if i < 0:
                return 0
            if arr[i] > total:
                return_val= _subset_adding_to_a_number(arr, total, i-1, cache)
            else:
                return_val= _subset_adding_to_a_number(arr, total, i-1, cache) + _subset_adding_to_a_number(arr, total-arr[i], i, cache)
            cache[key] = return_val
            return return_val

    return _subset_adding_to_a_number(arr, total, len(arr)-1, cache)

def knapsack(item, capacity):
    #cache
    cache = {}
    
    def _knapsack(item, available_capacity, i, cache):
        key = str(available_capacity) + ':' + str(i)
        try:
            return cache[key]
        except: 
            if i >= len(item):
                return 0
            if available_capacity <= 0:
                return 0
            if item[i][0] > available_capacity:
                return _knapsack(item, available_capacity, i+1, cache)
            else:
                value_including_i = item[i][1]+ _knapsack(item, available_capacity - item[i][0], i+1, cache) 
                value_excluding_i = _knapsack(item, available_capacity, i+1,cache)
                return_val= max(value_excluding_i, value_including_i)
                cache[key] = return_val
                return return_val

        
    return _knapsack(item, capacity, 0, cache)

def maximum_sum_continous_subarray(arr):
    local_sum = global_sum=0
    for i in range(len(arr)):
        local_sum = max(arr[i], local_sum+arr[i])
        global_sum = max(local_sum, global_sum)
    return global_sum





if __name__ == '__main__':
    #print(knapsack([(4,5),(2,3),(1,6)], 7))
    print(maximum_sum_continous_subarray([-2,-3,4,-1,-2,1,5,-3]))
