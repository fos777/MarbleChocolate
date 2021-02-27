# 问题:编写一个程序，以2位数字，X,Y作为输入，生成一个二维数组。数组的第i行和第j列中的元素值应该是i*j。
# 注意:
# i= 0,1 . .,X - 1;
# j = 0, 1,­..,Y - 1
# 例子假设程序有以下输入:3,5
# 则程序输出为:[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]
# 提示:注意:如果要为问题提供输入数据，应该假设它是一个控制台输入，以逗号分隔。
# 解决方案:
#%%
print('Please enter two numbers')

items = [int(x) for x in input().split(',')]
rowNum = items[0]
colNum = items[1]
multilist = [[0 for col in range (colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]=row*col

print (multilist)
# %%
