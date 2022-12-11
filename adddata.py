# adddata.py

f=open("C:/Users/jhw97/Desktop/개발/study/Python-prac/새파일.txt","a")
for i in range(11,21) :
    f.write("%d번째 줄입니다.\n" % i)
f.close()
