
import sys

fname = sys.argv[1]

with open(fname) as old:
    i = 0
    while 1:
        with open(fname+'-split-'+str(i), 'w') as new:
            data = old.read(1024*1024*3)
            if not data: break
            nextline = old.readline()
            while nextline and not nextline.startswith('WARC/1.0'):
                data += nextline
                nextline = old.readline()
            new.write(data)
            i += 1
