import time
    
def timeit(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        return result, t2 - t1
    return wrap_func


if __name__ == "__main__":
    
    @timeit
    def long_time():
        time.sleep(3)
    
    _, duration = long_time()
    print(f"duration: {duration}")