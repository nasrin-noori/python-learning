
# def permute(data,i,length):
#     result = []
#     if i == length:
#         result.append(''.join(data))
#     else:
#         for j in range(i,length):
#             data[i],data[j]=data[j],data[i]
#             result.extend(permute(data,i+1,length))
#             data[i],data[j]=data[j],data[i]
#     #print(result)        
#     return result
# # this function is o(n!) which n is number of shorter string character              
# #permute(list(s), 0, len(s))
# def asses_logic(export, search_string):
#     indicator=0
#     for k in range(0, len(export)):
#         if search_string.find(export[k]) != -1:
#             print('I found the permutation of', search_string, 'in the longer string, which is:', export[k])
#             indicator=1
#     if indicator!=1:
#         print('NO permutation found')

        
# if __name__ = '__main__':
#     t = input('enter longer string: ')
#     s = input('enter shorter string: ')
#     result = permute(list(s), 0, len(s))
#     asses_logic(result,t)
    #this function is o(n!*length of longer string)
    # TODO: optimize the algorithm to reach o(nm) where n is the length of the short and the m is the length of the long string
    # aaab vs abaa ? {a: 3, b: 1}
    # find abab in aabbbaaaba
####### first attepmt : the order of code is o(n^2*m)
def permute(short, long):
    short_list = list(short)
    long_list = list(long)
    for i in range(0, len(long_list) - len(short_list) + 1):
        num_right = 0
        for j in range(0, len(short_list)):
             if short_list.count(short_list[j])==long_list[i : i + len(short_list)].count(short_list[j]):
                if short_list[j] in long_list[i : i + len(short_list)]:  # Corrected indexing and condition
                     num_right += 1
        if num_right == len(short_list):
            yield long_list[i : i + len(short_list)]  # Corrected indexing


if __name__ == '__main__':
    t = input('Enter longer string: ')
    s = input('Enter shorter string: ')
    result = permute(s, t)
    for num in result:
        print(num)
####### second attempt : the order is o(n*m)
from collections import Counter

def permute(short, long):
    short_counter = Counter(short)
    long_list = list(long)
    short_length = len(short)
    for i in range(0, len(long) - short_length + 1):
        sub_list = long_list[i:i + short_length]
        if short_counter == Counter(sub_list):
            yield ''.join(sub_list)


if __name__ == '__main__':
    t = input('Enter longer string: ')
    s = input('Enter shorter string: ')
    result = permute(s, t)
    for num in result:
        print(num)
