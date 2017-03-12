import os
import threading
import time

import xillypy

read_device = '/dev/xillybus_read'
write_device = '/dev/xillybus_write'


def dump_data(dev_file, data_length):
    for _ in xillypy.stream_read(dev_file, length=data_length):
        pass


def benchmark(data_length):
    data = os.urandom(data_length)

    reader = threading.Thread(target=dump_data, args=(read_device, len(data)))
    reader.start()

    start_write = time.perf_counter()
    xillypy.stream_write(write_device, data)
    end_write = time.perf_counter()

    reader.join()

    bandwidth = len(data) / (10 ** 6) / (end_write - start_write)

    print('wrote {l:.2f} MB in {t:.3f} ms, bandwidth: {bw:.3f} MB/s'.format(l=len(data) / (10 ** 6),
                                                                            t=(end_write - start_write) * 1000,
                                                                            bw=bandwidth), flush=True)


if __name__ == '__main__':
    for factor in [6, 7, 8]:
        benchmark(10 ** factor)
