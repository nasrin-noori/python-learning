# python-learning
i=int(input ('give me the number of fibonacci series that you want "for example for example 10" : '))
import math
fi=1.618034
x = ((fi**i)-((1-fi)**i))/((math.sqrt(5)))
print('the amount of fibonacci wlii be',round(x))
resume=input('do you want to show before and after value ? if yes type "1" and if you dont want type "0"')
result=[0,1]
if resume=='1':
    #def fibonacci(length):
    result=[0,1]
    for j in range(2,(i+1)):
        result.append(result[j-1]+result[j-2])
print(result)


# TODO: write a recursive `function`` that calculates a nth fibonacci element.
# example: fibo(3) -> 2
# tests:
# assert fibo(2) == 2
# assert fibo(2) + fibo(3) == fibo(4)