import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x tld')
    os.system('./tld')
elif bit == '32bit':
    os.system('chmod +x tld32')
    os.system('./tld32')
else:
    print('device not supported')
