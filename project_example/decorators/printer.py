import functools
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


def shared_task(bind=False, priority=1, queue='long-running'):
    def wrapper_repeat(func):
        @functools.wraps(func)
        def wrapper_inner(*args, **kwargs):
            print('Before running task', args, kwargs, bind, priority, queue)
            result = func(*args, **kwargs)
            print('After running task', result)
            return result
        return wrapper_inner
    return wrapper_repeat



@shared_task(bind=True, priority=9, queue='short-running')
def handler(a, b):
    print('Running task', a, b)
    return a + b
