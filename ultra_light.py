# функция без параметров (1) и без возвращаемого значения (2)
def hi():
    print('Привет')

# функция с параметрами (1) и с возвращаемым значением (2)
def multiply_nums(a,b):
    return a*b

#lambda функция
a=lambda x: x+1
print(a(2))
# print((lambda x: x+1)(2))