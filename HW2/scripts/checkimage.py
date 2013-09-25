#!/usr/bin/env python
counter = 0
data = 0
with  open('../BadGuyThumb.dd','rb') as f:
    byte = f.read(1)
    while byte:
        byte = f.read(1)
        counter += 1
        if byte != b'\x00':
            data += 1
print 'total data',counter
print 'total non zero bytes',data