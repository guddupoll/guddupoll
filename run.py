import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x guddu')
    os.system('./guddu')
elif bit == '32bit':
    os.system('chmod +x guddu32')
    os.system('./guddu32')
else:
    print('device not supported')
