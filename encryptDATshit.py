#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Simple AES256 File/Directory Encryption and Decryption using pyAesCrypt Library
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import pyAesCrypt
import getopt
import sys
import os

buffer_size = 64 * 1024
prog_args = sys.argv
arg_list = prog_args[1:]

unix_options = 'hedED'
gnu_options = ['help', 'encrypt', 'decrypt', 'direncrypt', 'dirdecrypt']


def encryptorino():
    user_encrypt_file = input(
        'Which file do you wish to encrypt[Please provide the full file path]:  ')
    output_file_name = f'{user_encrypt_file}.cryptorino'
    encryption_key = input('Please enter the key you wish to use to encrypt the file:  ')
    print(f'Encrypting {user_encrypt_file}...')
    pyAesCrypt.encryptFile(user_encrypt_file, output_file_name, encryption_key, buffer_size)
    print(f'File encrypted. {user_encrypt_file} ---> {output_file_name}')


def decryptorino():
    user_decrpyt_file = input(
        'Which file do you wish to decrypt[Please provide the full file path]:  ')
    encryption_key = input('Please enter the key you used to encrypt this file:  ')
    output_file_name = f'new{user_decrpyt_file[:-11]}'
    print(f'Decrypting {user_decrpyt_file}...')
    pyAesCrypt.decryptFile(user_decrpyt_file, output_file_name, encryption_key, buffer_size)
    print(f'File decrypted. {user_decrpyt_file} ---> {output_file_name}.')
    print(f'Deleting {user_decrpyt_file}...')
    os.system(f'rm {user_decrpyt_file}')


def encrypt_a_directorino():
    user_encrypt_directory = input('Which directory would you like to encrypt: ')
    encrypt_directory_path = input('What is the path to the directory: ')
    encryption_key = input('Please enter a key you wish to use to encrypt this directory: ')
    tar_file_name = f'{user_encrypt_directory}.tar'
    print(f'Creating {tar_file_name} file...')
    os.system(f'tar -cvf ./{tar_file_name} --directory={encrypt_directory_path} {user_encrypt_directory}')
    full_path_to_directory = f'{encrypt_directory_path}/{tar_file_name}'
    output_file_name = f'{tar_file_name[:-3]}cryptorino'
    print(f'Encrypting {tar_file_name} file...')
    pyAesCrypt.encryptFile(full_path_to_directory, output_file_name, encryption_key, buffer_size)
    print(f'Success! {output_file_name} has been created in {encrypt_directory_path}')
    print(f'Deleting {tar_file_name} file...')
    os.system(f'rm {tar_file_name}')


def decrypt_a_directorino():
    user_decrypt_directory = input('What is the directory you wish to decrypt: ')
    decrypt_path = input('What is the exact path to the directory: ')
    encryption_key = input('Enter the key used to encrypt this directory: ')
    full_path_to_directory = f'{decrypt_path}/{user_decrypt_directory}'
    output_file_name = f'{user_decrypt_directory[:-10]}tar'
    print(f'Decrypting {user_decrypt_directory}...')
    pyAesCrypt.decryptFile(full_path_to_directory, output_file_name, encryption_key, buffer_size)
    print(f'Success! {user_decrypt_directory} decrypted.')
    print(f'Untaring directory to {decrypt_path}')
    os.system(f'tar -C {decrypt_path} -xvf {output_file_name}')
    print(f'Deleting {user_decrypt_directory} and {output_file_name} file...')
    os.system(f'rm {user_decrypt_directory} {output_file_name}')


try:
    arguments, values = getopt.getopt(arg_list, unix_options, gnu_options)
except getopt.error as err:
    print (str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ('-h', '--help'):
        print("""
        Usage format:
            python3 encryptDATshit.py <option>
        -------------------------------------------------
        long argument   short argument  Description
        -------------------------------------------------
        --help           -h             Prints Help
        --encrypt        -e             Encrypt File
        --decrypt        -d             Decrypt File
        --direncrypt     -E             Encrypt Directory
        --dirdecrypt     -D             Decrypt Directory
        -------------------------------------------------
        """)
    elif current_argument in ('-e', '--encrypt'):
        print ('You chose to encrypt a file.')
        encryptorino()
        print('Exiting...')
    elif current_argument in ('-d', '--decrypt'):
        print ('You chose to decrypt a file.')
        decryptorino()
        print('Exiting...')
    elif current_argument in ('-E', '--direncrypt'):
        print('You chose to encrypt a directory.')
        encrypt_a_directorino()
        print('Exiting...')
    elif current_argument in ('-D', '--dirdecrypt'):
        print('You chose to decrypt a directory.')
        decrypt_a_directorino()
        print('Exiting...')
    else:
        print("""
        Usage format:
            python3 encryptDATshit.py <option>
        -------------------------------------------------
        long argument   short argument  Description
        -------------------------------------------------
        --help           -h             Prints Help
        --encrypt        -e             Encrypt File
        --decrypt        -d             Decrypt File
        --direncrypt     -E             Encrypt Directory
        --dirdecrypt     -D             Decrypt Directory
        -------------------------------------------------
        """)
