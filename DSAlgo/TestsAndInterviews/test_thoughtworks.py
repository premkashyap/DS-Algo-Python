def trick_n_treat(no_of_childrens, boxes_left):
    cache = {}

    def _trick_n_treat(no_of_childrens, boxes_left, cache):
        key = str(no_of_childrens) + '|' + ' '.join(str(x) for x in boxes_left)
        try:
            return cache[key]
        except:
            if no_of_childrens == 0:
                cache[key] = True
                return cache[key]
            if boxes_left is None or len(boxes_left) == 0:
                return False
            for index, val in enumerate(boxes_left):
                if val > no_of_childrens:
                    cache[key] = _trick_n_treat(no_of_childrens, boxes_left[index+1:], cache)
                elif val == no_of_childrens:
                    cache[key] = True
                else:
                    cache[key] = _trick_n_treat(no_of_childrens-val, boxes_left[index+1:], cache) or _trick_n_treat(no_of_childrens, boxes_left[index+1:], cache)
                return cache[key]
            return cache[key]
        
    return _trick_n_treat(no_of_childrens, boxes_left, cache)
            
no_of_test_cases = int(input())
results = []
for i in range(no_of_test_cases):
    no_of_boxes, *boxes= map(int, input().split())
    no_of_childrens = int(input())
    res = trick_n_treat(no_of_childrens, boxes)
    results.append(res)

for result in results:
    print('Yes' if result else 'No')

