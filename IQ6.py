from array import *
import binascii
arr=array('i', [1, 2, 3, 4, 5, 6])
print(arr)
bytesarr=bytes(arr)
print(bytesarr)
ml=binascii.hexlify(bytesarr)
print(ml)