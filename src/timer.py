# MIT (c) jtankersley 2019-05-19
import math
import time


# --------            --------
# --------  Combined  --------
# --------            --------


def _getParamsString(*args, **kwargs):
    params = ""
    for arg in args:
        params += f"{arg},"
    for kwarg in kwargs:
        params += f"{kwarg},"
    if len(params) > 0:
        params = params[0:len(params) -1]
    return params


def _getSecondDecimals(seconds):
    if seconds > 1:
        return 5 - math.floor(math.log(seconds))
    else:
        return 6

def printTimedResult(time_dict, result, func_name, *args, **kwargs):
    # example: printResult("name", result)
    begin = time_dict.get("begin", 0)
    begin_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin))
    end = time_dict.get("end", 0)
    end_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
    params = _getParamsString(*args, **kwargs)
    seconds_string = format(end - begin, f".{_getSecondDecimals(end - begin)}f")
    print(f"{func_name}({params}) = {result}; ({seconds_string} seconds)")


def runTimedResult(func, *args, **kwargs):
    # example: result = runTimed(func, *args, **kwargs)
    begin = time.time()
    result = func(*args, **kwargs)
    time_dict = {"begin":begin, "end":time.time()}
    printTimedResult(time_dict, result, func.__name__, *args, **kwargs)
    return result


def printTimedResult_dec(func):
    # example: result = decorated_func()
    def decorator(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        time_dict = {"begin":begin, "end":time.time()}
        printTimedResult(time_dict, result, func.__name__, *args, **kwargs)
        return result
    return decorator


# --------          --------
# --------  Result  --------
# --------          --------


def printResult(result, func_name, *args, **kwargs):
    # example: printResult("name", result)
    params = _getParamsString(*args, **kwargs)
    print(f"{func_name}({params}) = {result}")


def runResult(func, *args, **kwargs):
    # example: result = runTimed(func, *args, **kwargs)
    result = func(*args, **kwargs)
    printResult(result, func.__name__, *args, **kwargs)
    return result


def printResult_dec(func):
    # example: result = decorated_func()
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        printResult(result, func.__name__, *args, **kwargs)
        return result
    return decorator


# --------        --------
# --------  Time  --------
# --------        --------


def printTime(func_name, time_dict):
    # example: printTime("name", time_dict)
    begin = time_dict.get("begin", 0)
    begin_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(begin))
    end = time_dict.get("end", 0)
    end_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
    seconds_string = format(end - begin, f".{_getSecondDecimals(end - begin)}f")
    print(f"{func_name}() ran {seconds_string} seconds from {begin_string} to {end_string}")


def runTimed(func, *args, **kwargs):
    # example: result = runTimed(func, *args, **kwargs)
    begin = time.time()
    result = func(*args, **kwargs)
    time_dict = {"begin":begin, "end":time.time()}
    printTime(func.__name__, time_dict)
    return result


def printTime_dec(func):
    # example: result = decorated_func()
    def decorator(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        time_dict = {"begin":begin, "end":time.time()}
        printTime(func.__name__, time_dict)
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
