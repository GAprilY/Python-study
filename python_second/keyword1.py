from ast import keyword
import keyword
keyword.kwlist

print('\n')
print('r\n')

#列表推导式
# [表达式 for 变量 in 列表]  或者  [表达式 for 变量 in 列表 if 条件]
#eg.输出 = [函数 for 变量 in 范围 if 约束条件]
multiples = [i for i in range(30) if i%3 == 0]
multiples


#字典推导式
# {key_expr: value_expr for value in collection }
# {key_expr: value_expr for value in collection if condition}
#eg.输出 = {变量：表达式 for 变量 in 范围}
listnew = {'Google', 'Runoob', 'Taobao'}
newdict = {key: len(key) for key in listnew }
newdict

#集合推导式 
# { expression for item in Sequence }
# { expression for item in Sequence if conditional }
#eg. 输出 = {表达式 for 变量 in 范围}
setnew = {i**2 for i in (1,2,3)}
setnew 

#元组推导式
# (expression for item in Sequence )
# (expression for item in Sequence if conditional )
#eg.输出 = (表达式 for 变量 in 范围)
tuplenew = (i for i in range(10))
tuplenew 
tuple(tuplenew)