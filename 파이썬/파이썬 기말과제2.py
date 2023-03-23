from hashlib import sha256 as SHA
import codecs
import glob
import os.path

SIZE = 1024*256

def getFileHash(filename):
     sha = SHA()
     h = open(filename, 'rb')
     content = h.read(SIZE)
     while content:
         sha.update(content)
         content.h.read(size)
     h.close()

     hashval = sha.digest()
     return hashval

def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHasg(file2)

    if hashval1 == hashval2:
        print(hashval1)
        print(hashval2)
        print("Two Files are Same")
    else:
        print(hashval1)
        print(hashval2)
        print("Two Files are Differant")

def main():
    Path1 = 'C:/Users/cloua/Desktop/파이썬/해시값검증/검증1/**'
    Path2 = 'C:/Users/cloua/Desktop/파이썬/해시값검증/검증2/**'
    
    for filei in glob.iglob(Path1, recursive=True):
        if(os.path.isfile(filei)):
            file1 = filei
            
    for filej in glob.iglob(Path2, recursive=True):
        if(os.path.isfile(filej)):
            file2 = filej
    
    hashCheck(file1, file2)

main()

    
