# Q:编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。
# HINT:考虑使用range(#begin， #end)方法

l = []
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print (l)