# MIT, jtankersley, 2019-05-18
import time

def print_time_dec(func):
    # reference: https://www.geeksforgeeks.org/decorators-in-python/
    # example: @print_time_dec
    def decorator(*args, **kwargs): 
        begin = time.time() 
        func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin) 
    return decorator 

def timeit(method):
    # reference: https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
    # example: @timer(), @timer(time_dict={}), @timer(time_dict={'log_name': 'log'})
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000)
            )
        return result
    return timed