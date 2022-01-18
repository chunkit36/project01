from distutils.errors import DistutilsFileError
from importlib.machinery import EXTENSION_SUFFIXES
from signal import SIG_DFL
from socket import send_fds
import sre_compile


for a in range(100):
    print("apple")
    print("banana")

b =[]
def eat_apple():
    
    for a in range(100):
        b.append(3)


eat_apple()

print(b)