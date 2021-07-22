import os
import hashlib
import sys

print("============== Select Menu ==============")
print("(1) Hash Calculation (2) Hashset (3) Exit")
menu = int(input("Select >>> "))
if menu == 1:
    filename = input('FileName >>> ')
    f1 = open(filename, 'rb')
    data = f1.read()
    f1.close()

    md5 = hashlib.md5(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()

    print("============== Hash Result ==============")
    print("MD5: " + md5)
    print("SHA-1: " + sha1)
    print("SHA-256: " + sha256)

if menu == 2:
    print("Default Searching Path is C:\\Users\\parj2\\Downloads")
    hashset = input("MD5 HashSet >>> ")
    path_dir = "C:/Users/parj2/Downloads/"
    file_list = os.listdir(path_dir)
    print(file_list)

    dic = {}
    for i in file_list:
        print(i)
        f2 = open(path_dir+i,'rb')
        realdata = f2.read()
        f2.close()

        md5 = hashlib.md5(realdata).hexdigest()

        dic[i] = md5

        print("MD5: " + md5, end="\n\n")

    print("C:\\Users\\parj2\\Downloads ALL File MD5 Result Save!!")
    print(dic)

    for key, value in dic.items():
        if value == hashset:
            print("============== Success ==============")
            print("Detection: "+ path_dir +key)
            break
        # else:
        #     print("============== Fail ==============")
        #     print("No matching MD5 HashSet~~")
        #     sys.exit()

if menu == 3:
    print("What The Fuxx!!")
    sys.exit()

