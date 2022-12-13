# notepad.py

import sys

option = sys.argv[1]
#memo = sys.argv[2]
#sys.argv[0] : notepad.py

if option=="-a": #입력
    memo = sys.argv[2]
    f = open("memo.txt","a")
    f.write(memo)
    f.write("\n")
    f.close()

elif option=="-v": #출력
    f= open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)

