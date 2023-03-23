from hashlib import sha256 as SHA
import codecs

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

