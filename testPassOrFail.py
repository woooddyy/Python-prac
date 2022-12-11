# testPassOrFail.py

cnt = 0
marks = []
while cnt<5 :
    marks.append(int(input("시험 성적을 입력해주세요")))
    cnt+=1
number = 1
for mark in marks:
    if mark >= 60 : print("%d번 학생은 합격입니다."% number)
    else : print("%d번 학생은 불합격입니다." % number)
    number+=1
