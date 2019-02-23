#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Simple AES256 File Encryption and Decryption using pyAesCrypt Library
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import pyAesCrypt
import getopt
import sys
import os

bufferSize = 64 * 1024
progArgs = sys.argv
argList = progArgs[1:]

unixOptions = 'hedtT'
gnuOptions = ['help', 'encrypt', 'decrypt', 'direncrypt', 'dirdecrypt']


def encryptorino():
    eFile = input('Which file do you wish to encrypt[Please provide the full file path]:  ')
    outF = eFile + '.aes'
    eKey = input('Please enter the key you wish to use to encrypt the file:  ')
    pyAesCrypt.encryptFile(eFile, outF, eKey, bufferSize)
    return 'File ecrypted.'


def decryptorino():
    dFile = input('Which file do you wish to decrypt[Please provide the full file path]:  ')
    dKey = input('Please enter the key you used to encrypt this file:  ')
    outF = 'new' + dFile[:4]
    pyAesCrypt.decryptFile(dFile, outF, dKey, bufferSize)
    return 'File decrypted.'


def encryptADirectorino():
    eFolder = input('Which directory would you like to encrypt: ')
    ePath = input('What is the path to the directory: ')
    eKey = input('Please enter a key you wish to use to encrypt this directory: ')
    tarF = eFolder + '.tar'
    print('Creating .tar file...')
    os.system('tar -cvf ./' + tarF + ' --directory=' + ePath + ' ' + eFolder)
    eFile = ePath + '/' + tarF
    outF = tarF[:-3] + 'cryptorino'
    print('Encrypting .tar file...')
    pyAesCrypt.encryptFile(eFile, outF, eKey, bufferSize)
    print('Success! ' + outF + ' has been created in ' + ePath)
    print('Deleting original tar file...')
    os.system('rm -f ' + tarF)


def decryptaDirectorino():
    dFolder = input('What is the directory you wish to decrypt: ')
    dPath = input('What is the exact path to the directory: ')
    dKey = input('Enter the key used to encrypt this directory: ')
    dir = dPath + '/' + dFolder
    outF = dFolder[:-10] + 'tar'
    print('Decrypting directory...')
    pyAesCrypt.decryptFile(dir, outF, dKey, bufferSize)
    print('Success! ' + dFolder + ' decrypted.')
    print('Untaring directory to ' + dPath)
    os.system('tar -C ' + dPath + ' -xvf ' + outF)
    print('Deleting .crypt file...')
    os.system('rm -f ' + dFolder)


try:
    arguments, values = getopt.getopt(argList, unixOptions, gnuOptions)
except getopt.error as err:
    print (str(err))
    sys.exit(2)

for currentArgument, currentValue in arguments:
    if currentArgument in ('-h', '--help'):
        print('-------------------------------------------------')
        print('long argument   short argument  Description')
        print('-------------------------------------------------')
        print('--help           -h             Prints Help')
        print('--encrypt        -e             Encrypt File')
        print('--decrypt        -d             Decrypt File')
        print('--direncrypt     -t             Encrypt Directory')
        print('--dirdecrypt     -T             Decrypt Directory')
        print('-------------------------------------------------')
    elif currentArgument in ('-e', '--encrypt'):
        print ('You chose to encrypt a file.')
        encryptorino()
    elif currentArgument in ('-d', '--decrypt'):
        print ('You chose to decrypt a file.')
        decryptorino()
    elif currentArgument in ('-t', '--direncrypt'):
        print('You chose to encrypt a directory.')
        encryptADirectorino()
        print('Exiting...')
    elif currentArgument in ('-T', '--dirdecrypt'):
        print('You chose to decrypt a directory.')
        decryptaDirectorino()
        print('Exiting...')
