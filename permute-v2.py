t=input('enter longer string: ')
s=input('enter shorter string: ')
def permute(data,i,length):
    result=[]
    if i==length:
        result.append(''.join(data))
    else:
        for j in range(i,length):
            data[i],data[j]=data[j],data[i]
            result.extend(permute(data,i+1,length))
            data[i],data[j]=data[j],data[i]
    #print(result)        
    return result
              
#permute(list(s), 0, len(s))
def asses_logic(export, search_string):
    indicator=0
    for k in range(0, len(export)):
        if search_string.find(export[k]) != -1:
            print('I found the permutation of', search_string, 'in the longer string, which is:', export[k])
            indicator=1
    if indicator!=1:
        print('NO permutation found')
result = permute(list(s), 0, len(s))
asses_logic(result,t)