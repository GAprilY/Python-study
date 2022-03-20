# f = open('2.txt','a')
# f.write('aaa')
# f.close()

# f = open('test.txt')
# con = f.readline()
# content = f.readline()
# print(con)
# print(content)
# f.close()

# f = open('test.txt','r+')
# f.read()
# f.close()

# f = open('test.txt','r+')
# f.seek(3, 0)
# con = f.read()
# print(con)

# import os
# os.mkdir('aa')

# os.rmdir('aa')

# print(os.getcwd())

# import os
# # 需求1：把code文件夹所有文件重命名为python_xxxx
# # 1. 找到所有文件
# file_list = os.listdir()
# print(file_list)
# # 2. 构造名字
# for i in file_list:
#     # new_name = "python" + 源文件i
#     new_name = "python_" + i
# # 3. 重命名
# os.rename(i,new_name)





# import os
# flag = 2
# # 获取指定目录
# dir_name = './'
# # 获取指定目录的文件列表
# file_list = os.listdir(dir_name)
# # print(file_list)
# # 遍历文件列表内的文件
# for name in file_list:
#     # 添加指定字符
#     if flag == 1:
#         new_name = 'python_' + name
#     # 删除指定字符
#     elif flag == 2:
#         num = len('python_')
#         new_name = name[name:]
#     # 打印文件名，测试程序的正确性
#     print(new_name)
# 	# 重命名
#     os.rename(dir_name+name,dir_name+new_name)

# class Washer():
#     def wash(self): # self 调用该函数的对象
#         print('能洗衣服')
#         print(self)

# haier1 = Washer()
# haier1.wash()

# haier2 = Washer()
# haier2.wash()




# class Washer():
#     def print_info(self):
#         # 类里面获取实例属性 self.属性名
#         print(self.width)
#         print(self.height)
#         print(f'洗衣机的宽度是{self.width}')
#         print(f'洗衣机的高度是{self.height}')
# # 创建对象
# haier1 = Washer()

# # 添加实例属性
# haier1.width = 400
# haier1.height = 800

# # 对象调用
# haier1.print_info()


from mimetypes import init


class Washer():
    # 定义 _init_() ，添加实例属性,初始化
    def __init__(self):
        # 添加实例属性
        self.width = 400
        self.height = 800
    
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')
	# def print_info(self):
    #     # 类里面获取实例属性 self.属性名
    #     print(f'洗衣机的宽度是{self.width}')
    #     print(f'洗衣机的高度是{self.height}')

haier = Washer()
haier.print_info()


class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def print_info(self):
       print(f'洗衣机的宽度是{self.width}')  
       print(f'洗衣机的高度是{self.height}')
haier = Washer(40, 50)
haier.print_info()

class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return '这是海尔洗衣机说明书'

haier = Washer(40 ,50)
# 这是海尔洗衣机说明书
print(haier)

        
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __del__(self):
        print('{self}对象已经删除')
        
haier = Washer(40, 50)

# del haier




# 1.定义类 初始化属性 被烤和添加调料的方法 显示对象
class SweetPotato():
    def __init__(self):
        # 被烤时间
        self.cook_time = 0
        # 烤的状态
        self.cook_status = "生的"
        # 添加调料列表
        self.condiments = []
    def cook(self, time):
        # 计算整体时间
        self.cook_time += time
        # 状态地瓜
        if 0<= self.cook_time < 3:
            self.cook_status = "生的"
        elif 3<= self.cook_time < 5:
            self.cook_status = "半生不熟"
        elif 5<= self.cook_time < 8:
            self.cook_status = "熟了"
        elif 8<= self.cook_time:
            self.cook_status = "烤糊了"
    
    def add_condiments(self, condiment):
        # 添加调料函数
        self.condiments.append(condiment)
        
        
    def __str__():
        return f"这个地瓜被烤过的时间是{self.cook_time}, 状态是{self.cook_status}"
        
# 2.创建对象 测试属性
digua1 = SweetPotato()
print(digua1)

digua1.cook(2)
print(digua1)












