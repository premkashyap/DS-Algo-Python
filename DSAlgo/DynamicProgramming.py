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

def longest_common_subsequence_length(A, B):
    
    cache = {}

    def _longest_common_subsequence_recursive(A, B, len_A, len_B, cache):
        '''
            It is also called top down method as it breaks the problem into smaller problem. It is also called recursive method
        '''
        if len_A == 0 or len_B == 0 or len(A) == 0 or len(B) == 0:
            return 0
        key = str(len_A) + "|" + str(len_B)

        if key in cache.keys():
            return cache[key]
        else:
            if A[len_A -1] == B[len_B - 1]:
                return _longest_common_subsequence_recursive(A, B, len_A-1, len_B-1, cache) + 1
            else:
                return max(_longest_common_subsequence_recursive(A, B, len_A-1, len_B, cache), _longest_common_subsequence_recursive(A, B, len_A, len_B-1, cache))
    
    
    def _longest_common_subsequence_iterative(A, B):
        len_A = len(A)
        len_B = len(B)

        if len_A == 0 or len_B == 0:
            return 0

        lookup = [[0 for i in range(len_B + 1)] for j in range(len_A + 1)]

        for i in range(1, len_A + 1):
            for j in range(1, len_B + 1):
                if A[i-1] == B[j-1]:
                    lookup[i][j] = lookup[i-1][j-1] + 1
                else:
                    lookup[i][j] = max(lookup[i][j-1], lookup[i-1][j])
        
        return lookup[len_A][len_B]
    
    return _longest_common_subsequence_iterative(A, B)

def longest_common_subsequence_iterative_length(A, B, lookup=None):
    len_A = len(A)
    len_B = len(B)

    if len_A == 0 or len_B == 0:
        return 0

    lookup = [[0 for i in range(len_B + 1)] for j in range(len_A + 1)]

    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if A[i-1] == B[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i][j-1], lookup[i-1][j])
    
    return lookup

def finding_longest_common_subsequence(A, B):
    len_A = len(A)
    len_B = len(B)
    lookup = longest_common_subsequence_iterative_length(A, B)
    def _finding_longest_common_subsequence(A, B, len_A, len_B):
        if len_A == 0 or len_B ==0:
            return ''
        elif A[len_A-1] == B[len_B-1]:
            return _finding_longest_common_subsequence(A, B, len_A-1, len_B-1) + A[len_A-1]
        elif lookup[len_A-1][len_B] > lookup[len_A][len_B-1]:
            return _finding_longest_common_subsequence(A, B, len_A-1, len_B)
        else:
            return _finding_longest_common_subsequence(A, B, len_A, len_B-1)

    return _finding_longest_common_subsequence(A, B, len_A, len_B)

def finding_all_longest_common_subsequence(A, B):
    len_A = len(A)
    len_B = len(B)
    lookup = longest_common_subsequence_iterative_length(A, B)
    def _finding_longest_common_subsequence(A, B, len_A, len_B):
        if len_A == 0 or len_B ==0:
            return ['']
        elif A[len_A-1] == B[len_B-1]:
            list_of_subsequences = _finding_longest_common_subsequence(A, B, len_A-1, len_B-1)
            list_of_subsequences = [x+A[len_A-1] for x in list_of_subsequences if list_of_subsequences is not None]
            return list_of_subsequences
        elif lookup[len_A-1][len_B] > lookup[len_A][len_B-1]:
            return _finding_longest_common_subsequence(A, B, len_A-1, len_B)
        elif lookup[len_A-1][len_B] < lookup[len_A][len_B-1]:
            return _finding_longest_common_subsequence(A, B, len_A, len_B-1)
        else:
            left = _finding_longest_common_subsequence(A, B, len_A-1, len_B)
            top = _finding_longest_common_subsequence(A, B, len_A, len_B-1)
            return top + left

    return _finding_longest_common_subsequence(A, B, len_A, len_B)

def longest_palindrome_subsequence(A):
    len_A = len(A)
    cache = {}
    def _longest_palindrome_subsequence(A, i, j, cache):
        key = str(i) + '|' + str(j)
        if key in cache.keys():
            return cache[key]
        if i>j:
            return 0
        if i == j:
            return 1
        if A[i] == A[j]:
            cache[key] = _longest_palindrome_subsequence(A, i+1, j-1, cache) + 2
        else:
            cache[key] = max(_longest_palindrome_subsequence(A, i+1, j, cache), _longest_palindrome_subsequence(A, i, j-1, cache))
        return cache[key]
    
    return _longest_palindrome_subsequence(A, 0, len(A)-1, cache)


if __name__ == '__main__':
    #print(knapsack([(4,5),(2,3),(1,6)], 7))
    #print(finding_all_longest_common_subsequence('ABCBDAB', 'BDCABA'))
    print(longest_palindrome_subsequence('ABBDCACB'))