import functools
from time import time, sleep

def logged(func):
    @functools.wraps(func)
    def wrapped_function(*args, **kwargs):
        str_args = [str(arg) for arg in args]
        str_kwargs = [f'{key}={value}' for key, value in kwargs.items()]
        print(f'Calling {func.__name__}({", ".join(str_args + str_kwargs)})')
        start_time = time()
        func_result = func(*args, **kwargs)
        end_time = time()
        print(f'Called {func.__name__}({", ".join(str_args + str_kwargs)}) '
              f'returns {func_result} '
              f'in {end_time - start_time:.3f} secs.')
        return func_result
    return wrapped_function


if __name__ == '__main__':
    # Very simple test
    @logged
    def add(x, y):
        sleep(1)
        return x + y

    @logged
    def sub(x, y):
        sleep(2.5)
        return x - y

    assert add(1, y=2) == 3
    assert add(x=5, y=-9) == -4
    assert sub(7, y=3) == 4
    assert sub(x=1, y=8) == -7
