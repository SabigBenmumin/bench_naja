import time
import random
import os

def fibo(n):

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def cputest():
    print('cpu in testing')
    for i in range (40):
        fibo(i)

def memtest():
    print('mem in testing')
    num = []
    round = 100000
    for i in range (0,round,1):
        num.append(int(random.randint(0,9)))
    for i in range (2,round,1):
        num[i]+= num[i-1]+num[i-2]

def write_to_disk(file_path, data_size):
    start_time = time.time()

    with open(file_path, 'wb') as file:
        # Writing dummy data to the file
        file.write(b'\x00' * data_size)

    end_time = time.time()

    return end_time - start_time

def disktest():
    print('disk in testing')
    round = 10
    write_time = 0
    for r in range(round):
        file_path = 'test_file.txt'
        data_size = 1000000*1000  # 100 MB
        temp = write_to_disk(file_path, data_size)
        write_time+=temp
        os.remove(file_path)

    print(f"Disk Test Performance: {write_time:.4f} seconds")
    return write_time

def benching():
    print('benching starto!!')
    start = time.time()
    memtest()
    stop = time.time()
    mem_t = stop - start
    print(f"Memory test Performance: {mem_t:.4f} seconds")
    disk_t = disktest()
    start = time.time()
    cputest()
    stop = time.time()
    cpu_t = stop - start
    print(f"CPU test Performance: {cpu_t:.4f} seconds")
    return mem_t, disk_t, cpu_t