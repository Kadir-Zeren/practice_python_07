city_list = [['New York','London','Istanbul','Seoul']]
print(city_list[0][3][2])

print(range(1,11))

a = range(1,11)
print(type(a))
list(a)
print(list(range(2,15,2)))

mylist = [1,2,3,4,5]
print(mylist[:3])

harf = 'abcdefg'
mylist =list(harf)
print(len(mylist))
print(len(harf))

print(range(2,21,3))
print(range(2,21,-3))
print(range(21,2,-3))

harf = 'abcdefg'
harf += 'a'
print(harf)

mytuple = (1,2,3,4,5,6)
print(tuple('itop'))

mytuple2= 9,8,7,6,5

print(type(mytuple),type(mytuple2))

a = [1,2,3]
b = (1,2,3)
print(type(a),type(b))

mytuple = ("Solar",)
print(type(mytuple))

mix_tuple = ('11',11,[2,'two',('six',6)], (5,'fair'))
str_six = mix_tuple[2][2][0]
print(str_six)

str_six = mix_tuple[2][1:3]
print(str_six)

a = [1,2,3]
b = (1,2,3)

import sys

print(sys.getsizeof(a))
print(sys.getsizeof(b))