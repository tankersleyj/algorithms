# MIT (c) jtankersley 2019-05-19
import time


def print_time(func_name, time_dict):
    # example: print_time("name", time_dict)
    begin = time_dict.get("begin", 0)
    begin_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin))
    end = time_dict.get("end", 0)
    end_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
    print(f"time: [{func_name}] ran for [{round(end - begin, 4)}] seconds from [{begin_string}] to [{end_string}]")


def run_timed(func, *args, **kwargs):
    # example: result = run_timed(func, *args, **kwargs)
    begin = time.time()
    result = func(*args, **kwargs)
    print_time(func.__name__, {"begin":begin, "end":time.time()})
    return result


def print_time_dec(func):
    # example: result = decorated_func()
    def decorator(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print_time(func.__name__, {"begin": begin, "end": end})
        return result
    return decorator


def get_time_dec(func):
    # example: result, time_dict = decorated_func()
    def decorator(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, {"begin": begin, "end": end}
    return decorator
