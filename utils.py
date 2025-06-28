import time
import functools

def rate_limit_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "Rate limit" in str(e):
                print("Достигнут лимит запросов. Ожидание 15 минут...")
                time.sleep(900)
                return func(*args, **kwargs)
            raise
    return wrapper