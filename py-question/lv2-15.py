# 2级
# 题：编写一个程序，计算a + aa + aaa + aaaa的值，给定的数字作为a的值。假设为程序提供了以下输入：
# 9     然后，输出应该是： 11106
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
# 解：
print('please enter a number')
a = input()
n1 = int("%s" %a)
n2 = int("%s%s"
%(a,a))
n3 = int("%s%s%s"%(a,a,a))
n4 = int("%s%s%s%s"%(a,a,a,a))
print (n1+n2+n3+n4)