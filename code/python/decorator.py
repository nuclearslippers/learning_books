# learing decoder @
import time


# 写一个记录时间的装饰器

def time_count(fuc):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        fuc(*args, **kwargs)
        print("time cost: ", (time.time() - t1))
    return wrapper

@time_count
def hello(times = 2):
    # time.sleep(0.5)
    for i in range(times):
        print("hello world")

# hello(3)


# 前后打印begin call,end call
def log_beginend(text=None):
    def decoder(fuc):
        def wrapper(*args, **kwargs):
            # do something
            if text:
                print("begin call: ", text)
            fuc(*args, **kwargs)
            # do something
            if text:
                print("end call: ", text)
        return wrapper
    return decoder

@log_beginend("hi")
def hi(times = 3):
    for i in range(times):
        print("hi world")

hi(5)