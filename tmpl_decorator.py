from functools import wraps
# 0. Remember to call any required modules to support the wrapped function (func).

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
    # 1. Code to execute BEFORE calling the decorated function.

    # 2. Call the decorated function as required, returning its
    # result if needed.
        return func(*args, **kwargs)

    # 3. Code to execute INSTEAD of calling the decorated function
    return wrapper