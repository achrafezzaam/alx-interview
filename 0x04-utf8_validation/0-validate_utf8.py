#!/usr/bin/python3
''' Define the validUTF8 function '''


def validUTF8(data):
    ''' Check if a given data is UTF8 valid '''
    bytes_num = 0
    val_1 = 1 << 6
    val_2 = 1 << 7

    for elem in data:
        byte_val = 1 << 7
        if bytes_num == 0:
            while byte_val & elem:
                bytes_num += 1
                byte_val = byte_val >> 1
            if bytes_num == 0:
                continue
            if bytes_num == 1 or bytes_num > 4:
                return False
        else:
            if elem & val_1 or not (elem & val_2):
                return False
        bytes_num -= 1
    if bytes_num == 0:
        return True
    return False
