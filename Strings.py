'''
Finding the duplicate characters in a string
'''

def FindDupes(str):
    '''
    Find the duplicates in a given string: ex malayalam ans m, a, l 
    '''
    char_map = {}
    for c in str:
        try:
            char_map[c]=char_map[c]+1
        except KeyError:
            char_map[c]=1
    print({k:v for k,v in char_map.items() if v >=2})

def Anagram(baseStr, anagram):
    '''
    another method is to sort both the strings and then compare.
    another method is to iterate the first string. see if the the character exists in anagram. Delete the character and assign it to anagram and see if anagram is empty in the end
    '''
    char_map = {}
    for c in baseStr:
        try:
            char_map[c]=None
        except KeyError:
            pass
    for c in anagram:
        try:
            char_map[c]
        except KeyError:
            return False
    return len(baseStr) == len(anagram)

def reverse_using_recursion(str):
    length = len(str)
    if length <= 1:
        return str
    else:
        return reverse_using_recursion(str[length//2: length]) + reverse_using_recursion(str[:length//2])

def only_digits(str):
    for c in str:
        if ord(c) > ord('9') or ord(c) < ord('0'):
            return False
    return True

def count_of_vowels_consonats(str):
    vowels, consonants= (0,0)
    for c in str:
        if c in 'aeiouAEIOU':
            vowels+=1
        else:
            consonants +=1
    return (vowels, consonants)

def given_String_rotation(str1, str2):
    temp_str = str1[1:] + str1[:1]
    while temp_str != str1:
        if temp_str ==str2:
            return True
        temp_str = temp_str[1:] + temp_str[:1]
    return False

def palindrome(str):
    length = len(str)
    for i in range(length//2):
        if str[i] != str[length-i-1]:
            return False
    return True

def first_non_repeating_charater(str):
    pass
    # sorted_str = ''.join(sorted(str))
    # index = 0
    # while index != len(sorted_str):
    #     otherindex = index
    #     while sorted_str[otherindex] == sorted_str[otherindex+1]:
    #         otherindex +=1
    #     if otherindex == index:
    #         return sorted_str[otherindex]
    #     index=
        
def reverse_string(str):
    length = len(str)
    reverse_string= ''
    for c in range(length):
        reverse_string+=str[length-1-c]
    return reverse_string

def reverse_words_of_string(str):
    start, end, result=0, 0, ''
    for c in range(len(str)):
        if str[c] == ' ' or str[c] == '\t' or c==len(str)-1:
            start, end = end, c
            result+=reverse_string(str[start:end+1])
        print(c, start, end, result)
    return result

def permutations_of_string(str):
    _permutation_string('', str)

def _permutation_string(perm, str):
    if len(str) ==0:
        print(perm+str)
    for i in range(len(str)):
        _permutation_string(perm +str[i], str[:i]+str[i+1:])



if __name__ == '__main__':
    print(permutations_of_string('1234'))
