def my_decorator(arg):
    def inner_decorator(func):
        def wrapped(*args, **kwargs):
            print('before function')
            response = func(*args, **kwargs)
            print('after function')
            return response
        print('decorating', func, 'with argument', arg)
        return wrapped
    return inner_decorator


@my_decorator('foo')
def printer(a, b):
    print('in function')
    return a + b
