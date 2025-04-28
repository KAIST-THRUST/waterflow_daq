import sys
import struct

buffer = bytearray(100)

a = 0x03
b = 124742
c = 16
d = 3.264
e = 31.54

buffer = struct.pack('BIIdd', a, b, c, d, e)

type, time, size = struct.unpack('BII', buffer[0:12])

# size of doubles
size_d = size//8

# formatstr: 'ddd...'
formatstr = 'd'*size_d
raw_data = struct.unpack(formatstr, buffer[16:16+size])

print(raw_data)