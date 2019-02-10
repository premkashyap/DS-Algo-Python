def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1]=lst[j+1], lst[j]
    
    return lst

def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        if i == 0 or lst[i] > lst[i-1]:
            continue
        for j in range(i, 0, -1):
            if lst[j]<lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        smallest = i
        for j in range(i+1, n):
            if lst[smallest]>lst[j]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
    return lst

def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    lst = merge(merge_sort(lst[:n//2]),  merge_sort(lst[n//2:]))
    return lst

def quick_sort(lst, pivot = None):
    n = len(lst)
    if n <=1:
        return lst
    pivot = lst[n//2]
    (lesser_than_pivot, same_as_pivot, greater_than_pivot,) = split(lst, pivot)
    lst = quick_sort(lesser_than_pivot) + same_as_pivot + quick_sort(greater_than_pivot)
    return lst


def split(lst, pivot):
    n = len(lst)
    lesser_than_pivot = []
    greater_than_pivot = []
    same_as_pivot = []
    for i in range(n):
        val = lst[i]
        if val<pivot:
            lesser_than_pivot.append(val)
        elif val>pivot:
            greater_than_pivot.append(val)
        else:
            same_as_pivot.append(val)
    return (lesser_than_pivot, same_as_pivot, greater_than_pivot)
    

def merge(lst1, lst2):
    lst = []
    i=0
    j=0
    list1_length= len(lst1)
    list2_length= len(lst2)
    while i< list1_length and j < list2_length:
        if  lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i < list1_length:
        lst = lst + lst1[i:]
    if j < list2_length:
        lst = lst + lst2[j:]
    return lst

def count_sort(lst, min_range, max_range):
    count = [0 for i in range(max_range-min_range+1)]
    for item in lst:
        count[item-min_range] =  count[item-min_range]+1
    for index, item in enumerate(count):
        if index>=1:
            count[index] = count[index]+ count[index-1]
    output_lst = [0 for i in range(len(lst))]
    for index, item in enumerate(lst):
        output_lst[count[item-min_range]-1] = item
        count[item-min_range] = count[item-min_range]-1
    return output_lst

def bucket_sort(lst, min_range, max_range):
    no_of_elements_in_bucket = int((max_range-min_range)*10)
    bucket = [[] for i in range(no_of_elements_in_bucket)]
    n = len(bucket)
    for item in lst:
        bucket[int(n*item)].append(item)
    for item in bucket:
        item = insertion_sort(item)
    output_list=[]
    for item in bucket:
        for bucket_item in item:
            output_list.append(bucket_item)
    return output_list

def gnome_sort(lst):
    index =0
    n = len(lst)
    while index<n:
        if index ==0 or lst[index]>=lst[index-1]:
            index+=1
        else:
            lst[index], lst[index-1]= lst[index-1], lst[index]
            index-=1
    return lst

def pigeonhole_sort(lst, min_value, max_value):
    rng = max_value-min_value
    pigeonhole = [0 for i in range(rng+1)]
    for val in lst:
        pigeonhole[val-min_value]=val
    return pigeonhole


if __name__ == '__main__':
    #print(pigeonhole_sort([5,3,2,4,1], 1,5))
    print(count_sort([1, 4, 1, 2, 7, 5, 2], 0 ,9))