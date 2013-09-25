#!/usr/bin/env python
counter = 0
headers = []
trailers = []
data = []
with  open('../BadGuyThumb.dd','rb') as f:
    byte = f.read(1)
    while byte:
        byte = f.read(1)
        counter += 1
        if byte == b'\xFF':
            byte1 = f.read(1)
            counter += 1
            if byte1 == b'\xD8':
                byte2 = f.read(1)
                counter += 1
                if byte2 == b'\xFF':
                    byte3 = f.read(1)
                    counter += 1
                    if byte3 == b'\xE0':
                        print hex(ord(byte)),hex(ord(byte1)),hex(ord(byte2)),hex(ord(byte3))
                        data.append(byte)
                        data.append(byte1)
                        data.append(byte2)
                        data.append(byte3)
                        headers.append(counter)
                        while True:
                            byte4 = f.read(1)
                            counter += 1
                            data.append(byte4)
                            if byte4 == b'\xFF':
                                byte5 = f.read(1)
                                data.append(byte5)
                                counter += 1
                                if byte5 == b'\xD9':
                                    trailers.append(counter-2)
                                    break
print 'Intances of jpeg headers found',len(headers)
print 'Intances of jpeg trailers found',len(trailers)
for header in headers:
    print 'header of match',str(header-3)
    print 'sector where this file is located',str(header/512)
for trailer in trailers:
    print 'footer/trailer of match',str(trailer-3)
    print 'sector where this file is located',str(trailer/512)
print 'length of data array',len(data)
# print "let's fix the data in the array"
# data.extend(['\x00']*(512%(len(data)%512)))
# print 'length of data array after adding zeros', len(data)
with open('output/file.jpg','wb') as f:
    for b in data:
        f.write(b)
