import struct
from io import FileIO, BufferedWriter, BufferedReader

__author__ = 'pgenssler'


def memory_read(dev_file: str, address: int, width=1) -> tuple:
    """
    reads bytes from a rc2f memory file
    @param dev_file: the memory to use
    @param address: where to read
    @param width: how many bytes to read
    @return: the read bytes as a tuple
    @rtype: tuple
    """
    with open(dev_file, 'rb') as mem:
        mem.seek(address)
        data = mem.read(width)
        return struct.unpack('B' * width, data)


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


def stream_write(dev_file: str, data: bytes) -> int:
    """
    stream data into the device
    @param dev_file: the target device
    @param data: data to write, bytes object
    @return: how many bytes were written
    @rtype: int
    """
    with BufferedWriter(FileIO(dev_file, 'wb')) as fifo:
        wrote = 0
        data_len = len(data)
        while data_len > wrote:
            wrote += fifo.write(data[wrote:data_len])
        return wrote


def stream_read(dev_file: str, byte_width=4) -> tuple:
    """
    streams data from a file and yields the data as a tuple until eof
    @param dev_file: the file to read
    @param byte_width: how many bytes per yield
    """
    with BufferedReader(FileIO(dev_file, 'rb')) as fifo:
        data = fifo.read(byte_width)
        while data:
            yield struct.unpack('B' * byte_width, data)
            data = fifo.read(byte_width)
