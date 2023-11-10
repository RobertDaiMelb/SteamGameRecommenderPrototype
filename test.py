from collections import Counter

# 初始化Counter对象
dic = Counter()

arr = ['a', 'b', 'c']
# 更新Counter，计数值为1
dic.update(arr)

new_arr = ['a', 'b', 'c', 'd']
# 再次更新Counter，存在的元素计数值增加1
dic.update(new_arr)

# 转换Counter为普通字典
dic = dict(dic)
new = ['a', 'b']
total_sum = sum(dic.values())
print(total_sum)