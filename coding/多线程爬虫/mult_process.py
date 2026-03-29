import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

nums = [112272535095293] * 100


def task1(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def single_thread():
    for num in nums:
        task1(num)


def multi_thread():
    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(task1, nums))


def multi_process():
    with ProcessPoolExecutor() as executor:
        executor.map(task1, nums)


def main():
    # 单线程
    start = time.perf_counter()
    single_thread()
    single_time = time.perf_counter() - start

    # 多线程
    start = time.perf_counter()
    multi_thread()
    thread_time = time.perf_counter() - start

    # 多进程
    start = time.perf_counter()
    multi_process()
    process_time = time.perf_counter() - start

    print(f"数据量: {len(nums)} 个")
    print(f"单线程:  {single_time:.4f}s")
    print(f"多线程:  {thread_time:.4f}s")
    print(f"多进程:  {process_time:.4f}s")
    print(f"线程加速比: {single_time/thread_time:.2f}x")
    print(f"进程加速比: {single_time/process_time:.2f}x")


if __name__ == "__main__":
    main()
