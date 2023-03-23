import glob
import os, random, struct
from Cryptodome.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt_file(key, in_filename):

    chunksize=64*1024
    out_filename = in_filename + '.jpg'

    iv = os.urandom(16) 
    encryptor = AES.new(key ,AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

key = b'key is KDFS 2020'
startPath = 'C:/Users/cloua/Desktop/KDFS2020/빈/**'

#Encrypts all files recursively starting from startPath
for filename in glob.iglob(startPath, recursive=True):
    if(os.path.isfile(filename)):
        print('Encrypting> ' + filename)
        encrypt_file(key, filename)
        
