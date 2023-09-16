import os
import sys

print('args')

for arg in sys.argv:
    print('arg: ' + arg)

abs_pth = os.path.abspath(sys.argv[0])
your_dir = os.path.dirname(abs_pth)

for val in abs_pth,your_dir:
    print(val)
