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


def shared_task(**options):
    def create_shared_task(bind=False, priority=1, queue='long-running'):
        def _expose_caller(func):
            def _expose_caller_args(*args, **kwargs):
                print('Before running task', args, kwargs, bind, priority, queue)
                result = func(*args, **kwargs)
                print('After running task', result)
                return result
            return _expose_caller_args
        return _expose_caller

    return create_shared_task(**options)


@shared_task(bind=True, priority=9, queue='short-running')
def handler(a, b):
    print('Running task', a, b)
    return a + b
