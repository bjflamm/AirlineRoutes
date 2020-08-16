# Give string, find the first non-repeating char in it and return it's index. if it doesn't exist, return -1
# "bellevue" -> indexOf('b') = 0
# i in range(0, len(str1))

def nonrepeat(str1):
    
    # for i in str1:
    #     count = 0
    #     for j in str1:
    #         if i == j:
    #             count += 1
    #     if count == 1:
    #         return indexOf(i)
    

    for i in range(0, len(str1)-1): #O(n)
        count = 0
        for j in str1: #O(n)
            if str1[i] == j:
                count += 1
        if count == 1:
            return i
    return -1

    for i in str
     check if i in dict
     if so then dict[i] == 1
     dict[i] += 1

    for i in str
     i is in dict
     count == 1 then 
     return i


print(nonrepeat("$12$zzz"))
        
