# sub_dir_search.py

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname) # 해당 디렉터리 파일 리스트
        for filename in filenames:
            full_filename = os.path.join(dirname,filename)
            #디렉터리와 파일이름 합쳐주기

            if os.path.isdir(full_filename):
                search(full_filename)

            else :

                #확장자 구분
                ext = os.path.splitext(full_filename)[-1]
                if ext==".py":
                    print(full_filename)
    except PermissionError:
        pass
    
search("C:/")

