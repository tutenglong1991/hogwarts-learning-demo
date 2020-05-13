"""
一切皆对象,函数也是对象
"""
import logging


def hi(name="yasoob"):
    return "hi " + name


print("hi函数对象的内存地址：")
print(hi)
print("直接调用函数:" + hi())
# 将一个函数或方法可以赋值给变量,该变量为一个函数对象引用，也具有可调用性
greet = hi
# 打印出变量greet执行的函数引用地址，发现和hi函数指向的是同一个内存地址
print("变量greet的函数对象内存地址:")
print(greet)
# 调用该变量引用的函数对象hi，输出与hi()一致
print("调用变量指向的函数对象引用：" + greet())
# 删除旧的hi函数，看看会发生什么！
del hi
# 报错：name 'hi' is not defined
# print(hi())
# 那继续调用下变量指向的函数对象引用呢？
print("删除原来的函数后，调用变量指向的函数引用:" + greet())
# 继续打印出变量greet的函数对象引用内存地址，发现还是和前面一样的，不会受到原来hi函数内存地址的删除影响
print(greet)

"""
在函数中定义函数
"""


def hello(name="yasoob"):
    print("now you are inside the hello() function")

    def greet1():
        return "now you are in the greet1() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet1())
    print(welcome())
    print("now you are back in the hello() function")


hello()
# output:now you are inside the hello() function
#       now you are in the greet1() function
#       now you are in the welcome() function
#       now you are back in the hello() function

# 上面展示了无论何时你调用hello(), greet1()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：

# greet1()
# outputs: NameError: name 'greet' is not defined


"""
从函数中返回函数，其实并不需要再一个函数里去执行即调用另一个函数，我们也可以将其作为函数返回出来：
"""


def outerDef():
    print("outfunction")
    pass


def funcReturnOtherFuncObject(name="yasoob"):
    def greet2():
        return "now you are in the greet2() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet2
    else:
        return outerDef


fo_to_greet2 = funcReturnOtherFuncObject()
fo_to_welcome = funcReturnOtherFuncObject(name="test")
print(fo_to_greet2)
print(fo_to_greet2())
print(fo_to_welcome)

"""
将函数作为参数传递给另一个函数
"""


def func1():
    return "hi yasoob"


def doSomethingBeforeFunc1(func1):
    print("I am doing some boring work before excuting func1()")
    print(func1())


doSomethingBeforeFunc1(func1)

"""
我的第一个装饰器：现在你已经具备所有必需知识，来进一步学习装饰器真正是什么了。装饰器让你在一个函数的前后去执行代码
"""


def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove foul smell")


a_function_requiring_decoration()
# now a_function_requiring_decoration is wrapped by wrapTheFunction()
# 被装饰后还需要调用才能执行，目前a_function_requiring_decoration只是指向了装饰器返回的函数对象
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# 调用执行函数对象a_function_requiring_decoration
a_function_requiring_decoration()
"""
继续用@符号生成简短的装饰器，将上面代码进行修改
↓     ↓     ↓     ↓     ↓     ↓     ↓      ↓
↓     ↓     ↓     ↓     ↓     ↓     ↓      ↓ 
"""


@a_new_decorator
def b_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am another new function which needs some decoration to "
          "remove my foul smell")


b_function_requiring_decoration()
# 但还存在一个问题，如果我们运行如下代码输出类名为：wrapTheFunction：
print("\n")
# 输出应该是"b_function_requiring_decoration"才是我们想要的
print(b_function_requiring_decoration.__name__)

"""
幸运的是Python提供给我们一个简单的函数来解决这个问题，
那就是functools.wraps, 我们修改上一个例子来使用functools.wraps：
@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
这可以让我们在装饰器里面访问在装饰之前的函数的属性。
"""

from functools import wraps


def b_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@b_new_decorator
def b_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am another new function which needs some decoration to "
          "remove my foul smell")


print("\n")
print(b_function_requiring_decoration.__name__)

"""
装饰器的一些常用场景
"""

from urllib import request


# 授权(Authorization)
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#     return decorated


# 日志（Logging）
def logit(func):
    @wraps(func)
    def with_logging(*args):
        print(func.__name__ + "was called")
        return func(*args)

    return with_logging


@logit
def addition_func(x):
    """do some math"""
    return x + x


result = addition_func(4)

"""
带参数的装饰器
"""


# 在函数中嵌入装饰器
# 我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。

def log_wrap(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


# 需要注意此处与前面不传参的处理不一样，如上面装饰器没有带()，表示的不是包裹函数，默认会将下面的函数当做参数传递
# 而此处使用了包裹函数，包住了装饰器，故一定得带(),若写成log_wrap则会报没有传递参数错误

@log_wrap()
def myfunc1():
    pass


myfunc1()


@log_wrap(logfile="func2.log")
def myfunc2():
    pass


myfunc2()


# @use_logging(level="warn") 等价于 @decorator
def use_logging(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("------>" + param["name"])
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args, *kwargs)

        return wrapper

    return decorator


print("\n")


@use_logging(level="warn")
def foo(param):
    """decorator is interesting"""
    print(param)


param = dict()
param["name"] = "111111111"
foo(param)

"""
类装饰器
"""


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()


@Foo
class decoratedClass:
    def __init__(self):
        print("我是被类装饰器修饰的类")


decoratedClass()
