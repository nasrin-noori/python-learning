def fibo(len): 
    if len<=0:
        return 0
    elif len==1:
      return 1
    else:
      num_1=0
      num_2=1
      for i in range(2,len+1):
        result=num_1+num_2
        num_1=num_2
        num_2=result
    return(result)
assert fibo(2)==1
assert fibo(2)+fibo(3)==fibo(4)
   
    
# TODO: write it using Generators (keyword yield vs return)

def fibo_generator(n):
    num_1=0
    num_2=1
    yield num_1
    yield num_2
    for i in range(2, n+1):
        result=num_1+num_2
        num_1=num_2
        num_2=result
        yield result
fibo_sequence=fibo_generator(int(input('enter n :')))
for num in fibo_sequence:
    print(num)
