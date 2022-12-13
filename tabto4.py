# tabto4.py

import sys

src = sys.argv[1]
dst = sys.argv[2]

f=open(src)
tab_cntn = f.read()
f.close()

space_cntn = tab_cntn.replace("\t"," "*4)

f=open(dst,"w")
f.write(space_cntn)
f.close()
