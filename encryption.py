import pyAesCrypt

password = input('Insert password for file encryption: ')

#encrypt 
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

#decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)

