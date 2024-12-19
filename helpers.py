import os
import time
from contextlib import contextmanager

def read_input(test=False):
    file_name = 'test_input.txt' if test else 'input.txt'
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip('\n')

@contextmanager
def measure_time():
    start_time = time.perf_counter()
    yield
    sync_duration = (time.perf_counter() - start_time)
    minutes, seconds = divmod(sync_duration, 60)
    print(f"Completed in {int(minutes):02}:{seconds:06.5f}")


