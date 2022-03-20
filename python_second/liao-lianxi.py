name = 'tom'
age = 18
weight = 80.5

print('名字%s,年龄%s，体重%s' %(name,age,weight))
print(f'名字{name},年龄{age}，体重{weight}')



'''
i = 0
results = 0
while i <= 10:
    results += i
    i = i+1

print(results)

x = 1
results1 = 1
while x < 10:
    results1 *=x
    x = x+1
print(results1)
'''
'''
九九乘法表，就是行和列相等的数组
'''

j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i*j}', end='\t')
        i = i+1
    print()
    j = j+1


a = 'tom ji he'
print (a.find('tom'))
print (a.find('1'))
print (a.index('j'))


#字典遍历
dict1 = {'Name': 'Runoob', 'Age': 7, 'Names': '小菜鸟'}
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)

dict1.get(key)
len(dict1)
type(dict1)

























