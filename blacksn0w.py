import os, time, subprocess, sys
from tkinter import *
def blacksn0w(bootargs):
    x = open('.ba', 'w')
    x.write(bootargs)
    x.close()
    if sys.platform != 'darwin':
        os.abort()
    print(subprocess.getoutput("./pwnsn0w.sh"))    
blacksn0w('-v')
