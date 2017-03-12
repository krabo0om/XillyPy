import array
import struct

__author__ = 'Paul Genssler'


def memory_read(dev_file: str, address: int, length=1) -> tuple:
    """
    reads bytes from a rc2f memory file
    @param dev_file: the memory to use
    @param address: where to read
    @param length: how many bytes to read
    @return: the read bytes as a tuple
    @rtype: tuple
    """
    with open(dev_file, 'rb') as mem:
        mem.seek(address)
        data = mem.read(length)
        return struct.unpack('B' * length, data)


def memory_write(dev_file: str, address: int, data: tuple):
    """
    reads a byte from a rc2f memory file
    @param dev_file: the memory to use
    @param address: which byte to read
    @param data: a tuple of bytes to write
    """
    with open(dev_file, 'wb') as mem:
        mem.seek(address)
        mem.write(struct.pack('B' * len(data), *data))


def stream_write(dev_file: str, data) -> int:
    """
    stream data into the device
    @param dev_file: the target device
    @param data: data to write, iterable and slicable container (like a list) with bytes objects
    @return: how many bytes were written
    @rtype: int
    """
    with open(dev_file, 'wb') as fifo:
        wrote = 0
        data_len = len(data)
        while data_len > wrote:
            wrote += fifo.write(data[wrote:data_len])
        return wrote


def stream_read(dev_file: str, length=-1, chunk_size=2 ** 12):
    """
    reads data from the device into an array of chuck_size bytes and yields it
    @param dev_file: the target device
    @param length: how many bytes to read, -1 until eof
    @param chunk_size: how much data per read, low values impact performance
    """
    with open(dev_file, 'rb') as fifo:
        read = 0
        while length < 0 or read < length:
            data = array.array('b')
            try:
                yield data.fromfile(fifo, min(length - read, chunk_size))
                read += len(data)
            except EOFError:
                yield data
                break
