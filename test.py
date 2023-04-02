print ("hello world!")

import glob
import os, random, struct
from Cryptodome.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def decrypt(key, in_filename):

    chunksize=64*1024    
    out_filename = in_filename[:-3]


    with open(filename, 'rb') as infile:
        filesize = struct.unpack('<Q',infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16) 

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

key = b'key is KDFS 2020'

startPath = 'C:/Users/cloua/Desktop/KDFS2020/빈/**' 

#Encrypts all files recursively starting from startPath
for filename in glob.iglob(startPath, recursive=True):
    if(os.path.isfile(filename)):
        print('Encrypting> ' + filename)
        decrypt(key, filename)#복호화
