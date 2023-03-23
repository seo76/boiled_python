from hashlib import sha256 as SHA
import codecs
import glob
import os

SIZE = 1024*256

def getFileHash(filename):
     sha = SHA()
     h = open(filename, 'rb')
     content = h.read(SIZE)
     while content:
         sha.update(content)
         content = h.read(SIZE)
     h.close()

     hashval = sha.digest()
     return hashval

def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHash(file2)

    if hashval1 == hashval2:
        print("The Hash value of ", os.path.basename(file1), "is\n", hashval1,"\n")
        print("The Hash value of ", os.path.basename(file2), "is\n", hashval2,"\n")
        print("Two Files are Same")
    else:
        print("The Hash value of ", os.path.basename(file1), "is\n", hashval1,"\n")
        print("The Hash value of ", os.path.basename(file2), "is\n", hashval2,"\n")
        print("Two Files are Differant")

def Findfile():
    global file1, file2
    
    Path1 = 'C:/Users/cloua/Desktop/파이썬/해시값검증/검증1/**'
    Path2 = 'C:/Users/cloua/Desktop/파이썬/해시값검증/검증2/**'
    
    for file1 in glob.glob(Path1, recursive=True):
        if(os.path.isfile(file1)):
            print("First file is", os.path.basename(file1))
            
    for file2 in glob.glob(Path2, recursive=True):
        if(os.path.isfile(file2)):
            print("Second file is",os.path.basename(file2),"\n")
            
    
    


Findfile()
hashCheck(file1, file2)

























    
