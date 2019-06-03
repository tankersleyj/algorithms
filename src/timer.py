# MIT (c) jtankersley 2019-05-19
import math
import time


# --------            --------
# --------  Combined  --------
# --------            --------


def _get_params_string(*args, **kwargs):
    params = ""
    for arg in args:
        params += f"{arg},"
    for kwarg in kwargs:
        params += f"{kwarg},"
    if len(params) > 0:
        params = params[0:len(params) -1]
    return params


def _get_second_decimals(seconds):
    if seconds > 1:
        return 5 - math.floor(math.log(seconds))
    else:
        return 6

def print_timed_result(time_dict, result, func_name, *args, **kwargs):
    # example: print_result("name", result)
    begin = time_dict.get("begin", 0)
    begin_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin))
    end = time_dict.get("end", 0)
    end_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
    params = _get_params_string(*args, **kwargs)
    seconds_string = format(end - begin, f".{_get_second_decimals(end - begin)}f")
    print(f"{func_name}({params}) = {result}; ({seconds_string} seconds)")


def run_timed_result(func, *args, **kwargs):
    # example: result = run_timed(func, *args, **kwargs)
    begin = time.time()
    result = func(*args, **kwargs)
    time_dict = {"begin":begin, "end":time.time()}
    print_timed_result(time_dict, result, func.__name__, *args, **kwargs)
    return result


def print_timed_result_dec(func):
    # example: result = decorated_func()
    def decorator(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        time_dict = {"begin":begin, "end":time.time()}
        print_timed_result(time_dict, result, func.__name__, *args, **kwargs)
        return result
    return decorator


# --------          --------
# --------  Result  --------
# --------          --------


def print_result(result, func_name, *args, **kwargs):
    # example: print_result("name", result)
    params = _get_params_string(*args, **kwargs)
    print(f"{func_name}({params}) = {result}")


def run_result(func, *args, **kwargs):
    # example: result = run_timed(func, *args, **kwargs)
    result = func(*args, **kwargs)
    print_result(result, func.__name__, *args, **kwargs)
    return result


def print_result_dec(func):
    # example: result = decorated_func()
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        print_result(result, func.__name__, *args, **kwargs)
        return result
    return decorator


# --------        --------
# --------  Time  --------
# --------        --------


def print_time(func_name, time_dict):
    # example: print_time("name", time_dict)
    begin = time_dict.get("begin", 0)
    begin_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin))
    end = time_dict.get("end", 0)
    end_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
    seconds_string = format(end - begin, f".{_get_second_decimals(end - begin)}f")
    print(f"{func_name}() ran {seconds_string} seconds from {begin_string} to {end_string}")


def run_timed(func, *args, **kwargs):
    # example: result = run_timed(func, *args, **kwargs)
    begin = time.time()
    result = func(*args, **kwargs)
    time_dict = {"begin":begin, "end":time.time()}
    print_time(func.__name__, time_dict)
    return result


def print_time_dec(func):
    # example: result = decorated_func()
    def decorator(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        time_dict = {"begin":begin, "end":time.time()}
        print_time(func.__name__, time_dict)
        return result
    return decorator


def get_time_dec(func):
    # example: result, time_dict = decorated_func()
    def decorator(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        time_dict = {"begin":begin, "end":time.time()}
        return result, time_dict
    return decorator
