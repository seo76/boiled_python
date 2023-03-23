from hashlib import sha256 as SHA
import codecs
import glob
import os.path

SIZE = 1024*256

def getFileHash(filename):
     sha = SHA()
     with open(filename, 'rb') as infile:
         content = infile.read(SIZE)
         while content:
             sha.update(content)
             content=infile.read(SIZE)
         infile.close()

     hashval = sha.digest()
     return hashval

def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHash(file2)

    if hashval1 == hashval2:
        print(hashval1)
        print(hashval2)
        print("Two Files are Same")
    else:
        print(hashval1)
        print(hashval2)
        print("Two Files are Differant")

def Findfile():
    global file1, file2
    
    Path1 = 'C:/Users/cloua/Desktop/파이썬/해시값검증/검증1/**'
    Path2 = 'C:/Users/cloua/Desktop/파이썬/해시값검증/검증2/**'
    
    for file1 in glob.glob(Path1, recursive=True):
        if(os.path.isfile(file1)):
            print("First file is", file1)
            
    for file2 in glob.glob(Path2, recursive=True):
        if(os.path.isfile(file2)):
            print("Second file is",file2)
            
    
    


Findfile()
hashCheck(file1, file2)

























    
