#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Simple AES256 File Encryption and Decryption using pyAesCrypt Library
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import pyAesCrypt
import getopt
import sys

bufferSize = 64 * 1024
progArgs = sys.argv
argList = progArgs[1:]

unixOptions = 'hed'
gnuOptions = ['help', 'encrypt', 'decrypt']


def encryptorino():
    eFile = input('Which file do you wish to encrypt[Please provide the full file path]:  ')
    outF = eFile + '.aes'
    eKey = input('Please enter the key you wish to use to encrypt the file:  ')
    pyAesCrypt.encryptFile(eFile, outF, eKey, bufferSize)
    return 'File ecrypted.'


def decryptorino():
    dFile = input('Which file do you wish to decrypt[Please provide the full file path]:  ')
    dKey = input('Please enter the key you used to encrypt this file:  ')
    outF = dFile[:4] + '.raw'
    pyAesCrypt.decryptFile(dFile, outF, dKey, bufferSize)
    return 'File decrypted.'


try:
    arguments, values = getopt.getopt(argList, unixOptions, gnuOptions)
except getopt.error as err:
    print (str(err))
    sys.exit(2)

for currentArgument, currentValue in arguments:
    if currentArgument in ('-h', '--help'):
        print('--------------------------------------------')
        print('long argument   short argument  Description')
        print('--------------------------------------------')
        print('--help           -h             Prints Help')
        print('--encrypt        -e             Encrypt File')
        print('--decrypt        -d             Decrypt File')
        print('--------------------------------------------')
    elif currentArgument in ('-e', '--encrypt'):
        print ('You chose to encrypt a file.')
        encryptorino()
    elif currentArgument in ('-d', '--decrypt'):
        print ('You chose to decrypt a file.')
        decryptorino()
