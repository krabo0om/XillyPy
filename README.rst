XillyPy
=======
A simple Xillybus interface written in Python.
It supports streaming as well as reading/writing bytes to an address/data interface.

Usage
=====
.. code:: python

  import xillypy
  # write 16 (0x10, 0b00010000) to address 2
  xillypy.memory_write('/dev/xillybus_mem', 2, (16,))
  # write some bytes (.encode()) to a streaming interface
  xillypy.stream_write('/dev/xillybus_write', 'this is my data i want to write'.encode())



An example can be found in `benchmark.py <https://github.com/krabo0om/XillyPy/blob/master/benchmark.py>`_.

Compatibility
=============
The code was tested with Python 3.5 and 3.6 on a Linux Host (Ubuntu 16.04).


