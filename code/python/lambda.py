# learning lambda

# 实现下面函数的lambda
def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))

print(L1)

L2 = list(filter(lambda n: n%2 ==1, range(1, 20)))

print(L2)