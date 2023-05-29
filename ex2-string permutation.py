
result = [] # this is not a best practice
def permute(data, i, length):
    # first solution: define `results` here.
    # second solution: as an input variable.
    # third solution: use `yield` instead of `return`
    # forth solution: tail recursive instead of simple recursion.
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i,length):
            # swap
            data[i], data[j] = data[j], data[i]
            print(data)
            permute(data, i + 1, length)
            print('i: ',i)
            data[i], data[j] = data[j], data[i] 

# def main_logic(input_1, input_2, ...):
    # do you logic
    # return result

if __name__ == '__main__':
    t = input('enter your prefferd string: ')
    s = input('eneter your shorter string: ')
    # returns first occurrence of Substring
    export = t.find(s)
    if t.find(s) !=-1:
        print("shorter string which is",s," found")
    else:
        print("shorter string which is : ",s, " DIDNOT found at index")
    print("Initial string", s)
    
    permute(list(s), 0, len(s))
    
    # Printing result
    print("Resultant permutations", str(result))
    # PART 1
    ndicator=int
    for k in range(0,len(result)):
        if t.find(result[k])!=-1:
            print('I found the permutation of',s,'in longer string which is: ', result[k] )
            indicator=1
    if indicator!=1:
        print('NO NO Dear')
    # END OF PART 1
    
    # TODO: what is the order of this algorithm. (asymptotic analysis) 
    # for example: the below algorithm is of order o(n)
    # for i in range(0, n):
    #     i * i

    # TODO: create a function out of part 1

    # TODO: find a way to remove the global variable `results``.

    # TODO: use itertools.permutations instead of your self-defined `permute`
