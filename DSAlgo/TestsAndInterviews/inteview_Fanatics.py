def longest_substring(string):
    substr = ''
    cache = {}
    def _longest_substring(string, i, substr, cache):
        #input()
        key = substr+ str(i)
        if key in cache.keys():
            return cache[key]
        if string == '' or i > len(string)-1:
            return ''
        if string[i] not in substr:   
            substr+=string[i]
            cache[key] = _longest_substring(string, i+1, substr, cache) 
        else:   
             #index of current substring in string +1
            index = len(substr)
            new_substr = _longest_substring(string, i-index +1,'', cache)            
            cache[key] = new_substr if len(new_substr) > len(substr) else substr
        return cache[key]
          
    substr = _longest_substring(string, 0, substr, cache)
    return len(substr)
 
print(longest_substring('abcadefb'))