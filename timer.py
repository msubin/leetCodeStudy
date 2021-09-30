import time
import datetime


def timer(func):
    """Print the runtime of the decorated function."""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter_ns()
        value = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        run_time = (end_time - start_time)
        print(f"Finished {func.__name__!r} in {run_time} nanoseconds")
        return value
    return wrapper_timer