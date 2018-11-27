def odd(m):
    if m % 2 == 0:
        return True


# filter是把函数应用到序列，结果为True的保留下啦
if __name__ == '__main__':
    nums = range(10)
    l = list(filter(odd,nums))
    print(l)
