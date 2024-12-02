from collections import deque

# deque 是一个双向队列，队列的作用是存储数据，然后可以从队列的头部和尾部添加和删除数据
# 队列的元素可以通过q[0]和q[-1]获取，也可以通过q.popleft()和q.pop()获取
# deque 适用于需要频繁添加和删除数据的场景，例如爬虫的url队列
q = deque(['a', 'b', 'c'])

# 队列的元素可以从队列的头部和尾部添加和删除
q.append('x') # 从队列的尾部添加元素
q.appendleft('y') # 从队列的头部添加元素
print(q)