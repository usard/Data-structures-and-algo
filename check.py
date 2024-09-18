
# def isPowerOfTwo( n: int) -> bool:
#     if n == 1 :
#         return True
#     else :
#         if n < 1:
#             return False
#         else:
#             return True and isPowerOfTwo(n/2)
    
# isPowerOfTwo(16)

# def isPowerOfThree( n: int) -> bool:
#         if n == 3 or 1 :
#            return True
#         else:
#             if n <= 0:
#                return False
#             else :
#                 return True and isPowerOfThree(n/3)

# print(isPowerOfThree(0))    


# def swapPairs(self, head):
#     if not head or not head.next:
#         return head
#     temp = head.next
#     head.next = swapPairs(head.next.next)
#     temp.next = head
        
#     return temp

# def removeDuplicates(str):
#     i,j=0,1
#     str1=[]
#     while i < j :
#         if str[i] != str[j]:
#             str1.append(str[i])
#             i = i+1
#             j = j+1
#         else:
#             if str[j] == str[j+1]:
#                 j = j +1
#                 pass
#             else:
#                 i = i -1
#     print(str1)           
           
# removeDuplicates('azxxzbc')        


def tail_recurs_sum_natural(n):  # tail recursion
    if n == 1: 
        return 1
    if n == 0:
        return 0
    return n+sum_natural(n-1)

def head_recur_sum_natural(n, total=0):
    if n <=1:
        return total
    return head_recur_sum_natural(n-1, n+total)

def tail_prod_numbers(x,y):
    if y == 1:
        return x
    if y == 0:
        return 0
    return x+tail_prod_numbers(x, y-1) 

def is_palindrome(str):
    n = len(str)-1
    i=0
    while i<n:
        if str[i] == str[n]:
            i=i+1
            n=n-1
        else:
            return False
    return True

# print(is_palindrome('malayalam'))
     
def printPalindromes(str):
    for i in range(0,len(str)):
        for j in range(i, len(str)):
            if is_palindrome(str[i:j+1]):
                print(str[i:j+1])

# print(printPalindromes('malayalam'))

# def printCombinations(str):
#     n = len(str)
#     for i in range(0,n):
#         for j in range(i,)

def print_combinations(str):
    n=len(str)
    for h in range(0,n):
        for i in range(h,n):
            for j in range(h,i+1):
                print(str[j], end='')
            print('')
    

# print_combinations('geeeks')


# **************STRINGS******************

# reverse string
# loops
def reverse_string(str):
    n = len(str)
    str_list = list(str)
    for i in range(int(n/2)):
        temp=str_list[i]
        str_list[i]=str_list[n-1-i]
        str_list[n-1-i] = temp
    return "".join(str_list)

# print(reverse_string('geeksl'))

# recursion

def reverse_string_recursi(str,first,last):
    str_list = list(str)
    temp= str_list[first]
    str_list[first] = str_list[last]
    str_list[last] = temp
    str = "".join(str_list)
    if first >= last:
        return str
    else:
      return  reverse_string_recursi(str,first+1, last-1)
    

# right rotate a string by 2

def right_rotate_string(str,d):
    str_list = []
    n=len(str)
    for i in range(d,n,1):
        str_list.append(str[i])
    for i in range(0,d):
        str_list.append(str[i])
    
    return ''.join(str_list)

# print(right_rotate_string('malayalam', 2))  # T: O(n), S: O(n)

# by recursion

def rotate_string_right_recursion(str, d):
    if d == 0 or d > len(str):
        return str
    else:
        return rotate_string_right_recursion(str[1:]+str[0],d-1)

# print(rotate_string_right_recursion('kohli', 2))

def rotate_string_left_recursion(str, d):
    if d == 0 or d > len(str):
       return str
    else:
        return rotate_string_left_recursion(str[-1]+str[0:-1], d-1)

# print(rotate_string_left_recursion('kohli', 2))


def sort_string(str):
    n= len(str)
    str = list(str)
    for i in range(0,n):
       for j in range(i+1,n-1):
           if str[i] > str[j]:
               str[i], str[j] = str[j], str[i]
    return "".join(str)

# print(sort_string('bbccdefbbaa'))       


def freq_characters(strng):
    freq=''
    increment=1
    for i in range(0,len(strng), increment): # you cannot dynamically update increment value from inside
        count=1
        for j in range(i+1, len(strng)):
            if strng[i] == strng[j]:
                count+=1
        freq = freq+strng[i]+str(count)  
        increment=count
    return freq      


# print(freq_characters('aabccccddd'))

def freq_characters_using_map(str):
    mp={}
    n=len(str)
    for i in range(0,n):
        print('get', mp.get(str[i]))
        if mp.get(str[i]) != None:
            mp[str[i]] = mp.get(str[i])+1
        else:
            mp[str[i]] = 1
    # print(mp)
    mapKeys = list(mp.keys())
    mapKeys.sort()
    for i in mapKeys:
        print(i,end='')
        print(mp[i], end='')

freq_characters_using_map('bbccdefbbaa')

# print(reverse_string_recursi('geeks',0,4))



    
# reverse_string('undertaker')



