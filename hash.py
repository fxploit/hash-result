import sys
import hashlib

file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("Syntax Error!!\n")
    sys.exit()

f = open(file_path, 'rb')
data = f.read()
f.close()

print("=========== Hash Result ===========")
print("MD5: " + hashlib.md5(data).hexdigest())
print("SHA-1: " + hashlib.sha1(data).hexdigest())
print("SHA-256: " + hashlib.sha256(data).hexdigest())