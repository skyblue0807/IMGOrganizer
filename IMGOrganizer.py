import os

#일단 1) 사람에게 경로를 받음 (일단 1개) -이후에 여러개로 확장
# 2) 보고서를 쓰기 위한 파일명을 생성(일시 + 랜덤수 3개)
# 3) 보고서를 이름으로 해서 .txt 생성

path = input("주소를 입력하세요 (1개만)")
path_list = path.split(os.path.sep)
path = ""
for i in path_list:
    if path == "":
        path = i
    else:
        path = path + '/' + i

print(os.listdir(path))