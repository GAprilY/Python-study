# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    print(my_abs(-99))


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
#
# def nop():
#     pass
# 缺少了pass，代码运行就会有语法错误。


# 函数的参数
# 位置参数
# 我们先写一个计算x2的函数：

def power(x):
    return x * x


# 对于power(x)函数，参数x就是一个位置参数。
#
# 当我们调用power函数时，必须传入有且仅有的一个参数x：
# >>> power(5)
# 25
# >>> power(15)
# 225
# 现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。
#
# 你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


'''# 对于这个修改后的power(x, n)函数，可以计算任意n次方：
#
# >>> power(5, 2)
# 25
# >>> power(5, 3)
# 125
# 修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

# 默认参数
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
'''


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 设置默认参数时，有几点要注意：
#
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#
# 二是如何设置默认参数。
#
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。


# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
#
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 但是调用的时候，需要先组装出一个list或tuple：
# >>> calc([1, 2, 3])
# 14
# >>> calc((1, 3, 5, 7))
# 84
# 如果利用可变参数，调用函数的方式可以简化成这样：
#
# >>> calc(1, 2, 3)
# 14
# >>> calc(1, 3, 5, 7)
# 84
# 所以，我们把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


'''# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
# >>> calc(1, 2)
# 5
# >>> calc()
# 0
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
# >>> nums = [1, 2, 3]
# >>> calc(nums[0], nums[1], nums[2])
# 14
# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
# >>> nums = [1, 2, 3]
# >>> calc(*nums)
# 14
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
'''

'''递归函数，斐波那契数列'''
'''fact(n) = n! = 1X2X3X...X(n-1)Xn = fact(n-1)Xn'''


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


fact(10)
'''递归函数的优点是定义简单，逻辑清晰。
理论上，所有的递归函数都可以写成循环的方式，
但循环的逻辑不如递归清晰。
使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，
栈就会减一层栈帧。由于栈的大小不是无限的，
所以，递归调用的次数过多，会导致栈溢出。
'''
'''
解决递归调用栈溢出的方法是通过尾递归优化，
事实上尾递归和循环的效果是一样的，所以，
把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，
并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，
使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''
'''例子如递归函数'''

'''
def fact_iter(num, product):
    if num ==1:
        return product
    return fact_iter(num-1, num * product)
    pass


def fact(n):
    return fact_iter(n,1)

fact(10)
'''

###
'''
把一个list中所有的字符串变成小写：
'''
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
###


'''
生成器-generator   yield
'''
# 方法1
L = [x * x for x in range(10)]
L
# Out[3]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 方法2
# next(g)到元素结束
g = (x * x for x in range(10))
g
next(g)
'''generator保存的是算法，每次调用next(g)，太麻烦，一直next(g)，第二种写法'''
g = (x * x for x in range(10))
for n in g:
    print(n)

'''杨辉三角-廖雪峰'''


def triangles():
    p = [1]
    while True:
        yield p  # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

'''迭代器 iterable   isinstance() 验证
可作用于for循环和next()函数不断调用返回值
'''
from collections.abc import Iterable

isinstance([], Iterable)

# 判断一个对象是否为iterable对象：

from collections.abc import Iterator

isinstance((x for x in range(10)), Iterator)  # 判断一组数为iterable
isinstance([], Iterator)
isinstance({}, Iterator)  # 判断一个字符
isinstance('ABC', Iterator)  # 判断一组字符

'''高阶函数
map()  接收2个参数，一个是函数，一个是iterable
filter()
sorted()
'''
# map()  接收2个参数，一个是函数，一个是iterable
# 例如： f(x)=x^2
def f(x):
    return x * x
r = map(f, [1,2,3,4,5,6,7,8,9])
list(r) # iterable是惰性序列，需要通过list()计算出来

# 普通实现方式
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

# map() 可以计算人以复杂的函数 代码简单只需要一行
list(map(str,[1,2,3,4,5,6,7,8,9]))

# reduce() 把一个函数作用在一个序列中，必须接收两个参数
# reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
# 例如序列求和问题,通常使用sum求和
''' 
sum(iterable[, smart]) 
iterable -- 可迭代对象，如：列表、元组、集合。
start -- 指定相加的参数，如果没有设置这个值，默认为0。
sum([0,1,2])
out:3
sum((2,3,4),1)
out:10
sum([0,1,2,3,4],2)
out:12
'''
from functools import reduce
def add(x,y):
    return x+y
reduce(add, [1,3,5,7,9])

# 序列[1,3,5,7,9]→12579→reduce
from functools import reduce
def fn(x,y):
    return x*10+y
reduce(fn,[1,3,5,7,9])
# 字符串序列使用reduce
#方式1
from functools import reduce
def fn(x,y):
    return x*10+y
def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
reduce(fn, map(char2num, '13579'))
#方式2
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
