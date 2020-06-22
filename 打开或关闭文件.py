import os
##r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
##rb  以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
##w   打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。



##打开文件
file=open("foo.txt","w")
print (file.name) #文件名
print(file.mode)  #访问模式
print(file.closed)#是否已关闭


#关闭文件
file.closed()




#写  write()
file=("foo.txt",'w')
file.write("hello word!\nvery good")
file.closed()




#重命名和删除文件，重命名将test1命名为test2
os.rename('test1.txt','test2.txt')


os.remove('test2.txt')



# mkdir()方法
# 可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
#
# 语法：

os.mkdir("newdir")


# chdir()方法
# 可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
#
# 语法：
os.chdir("/home/newdir")


# getcwd()方法：
#
# getcwd()方法显示当前的工作目录。
#
# 语法：

os.getcwd()