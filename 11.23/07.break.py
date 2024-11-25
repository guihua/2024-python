n = 1

# while 循环, 只要条件满足，就不断循环，条件不满足时退出循环
# break 语句可以在循环过程中直接退出循环，而 continue 语句可以跳过当前的这次循环，直接开始下一次循环
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

while n <= 100:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)