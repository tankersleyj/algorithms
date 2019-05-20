# MIT (c) jtankersley 2019-05-19
import time


def print_time_dec(func):
    # decorator
    # example: result = func()  # (decorated with @print_time_dec)
    def decorator(*args, **kwargs): 
        begin = time.time()
        begin_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin))
        result = func(*args, **kwargs) 
        end = time.time()
        end_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
        print(f"{func.__name__} ran for {round(end - begin, 4)} seconds from {begin_string} to {end_string}") 
        return result
    return decorator 


def log_time_dec(func):
    # decorator
     # example: result, time_dict = func()  # (decorated with @log_time_dec)
    def decorator(*args, **kwargs):
        begin = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 
        return result, {"seconds": end - begin, "function": func.__name__}
    return decorator
