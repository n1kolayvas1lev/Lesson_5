import time
from collections import OrderedDict
from functools import lru_cache
def fab_decorator(arg1):
    print('Аргумент ф. декораторов.')
    def decorator(fn):
        print('Вызываюсь при декорировании. С аргументом из фабрики декораторов.')
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@fab_decorator(123)
def test(): #test = decorator(test)
    print('Ty kurwa!')
    ...

def cache(size = 3):
    def decor_cache(fn):
        cache_dict = OrderedDict()
        def wrapper(*args):
            if args not in cache_dict:
                if len(cache_dict) == size:
                    cache_dict.popitem(last=False)
                result = fn(*args)
                cache_dict[args] = result
            return cache_dict[args]
        return wrapper
    return decor_cache
#@cache()
@lru_cache(maxsize=3) #альт. вар. кеширования
def my_sleep():
    time.sleep(3)
if __name__ == '__main__':
    t0 = time.time()

    my_sleep()
    my_sleep()
    print(time.time() - t0)