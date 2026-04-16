import time
def running_2000(function, *args, **kwargs):
    start = time.perf_counter()

    function(*args, **kwargs)
    
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print(running_2000("Hi {name}".format, name="Bug"))