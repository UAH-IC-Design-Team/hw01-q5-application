import random
import string

files = 1000
size = 1024*1024


for i in range(files):
    filename = ''.join([random.choice(string.ascii_letters) for i in range(10)])
    chars = ''.join([random.choice(string.printable) for i in range(size)])
    with open("data/"+filename+'.txt', 'w') as f:
        f.write(chars)


