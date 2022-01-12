from functools import reduce
# take out even numbers from the list
nums = [3,4,6,5,8,7,0]

even_list = list(filter(lambda n : n%2 ==0,nums))
print(even_list)

f = lambda a : a**(1/2)
print(round(f(3),2))

f1 = lambda a,b : a+b
print(f1(5,5))

# print double value of each element in even list

double_even_list = list(map(lambda a : a*2, even_list))
print(double_even_list)

total_list = reduce(lambda a,b: a+b,nums)
print(total_list)



