import os
import datetime as dt
import random
import pandas as pd

#일단 1) 사람에게 경로를 받음 (일단 1개) -이후에 여러개로 확장
# 2) 보고서를 쓰기 위한 파일명을 생성(일시 + 랜덤수 3개)
# 3) 폴더 속 파일 리스트, 생성일, 크기를 csv파일로 저장 // https://mentha2.tistory.com/207
# 4) 파일 리스트를 report 폴더 내에 csv로 저장

#보고서 이름명 생성
case_name = dt.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randrange(0, 10)) + str(random.randrange(0, 10))
print('case:', case_name)

# path = input("주소를 입력하세요 (1개만)")
path = 'C:\Code_Practice\IMGOrganizer'
path_list = path.split(os.path.sep)
path = ""
for i in path_list:
    if path == "":
        path = i
    else:
        path = path + '/' + i

flist = os.listdir(path) #List 형태로 받아옴

for fname in flist:
    if not os.path.isdir(path+'/'+fname):
        print(fname)

df_list = pd.DataFrame(flist)
df_list.columns=['file_names']

report_path = os.path.join(os.path.join(os.getcwd(), 'report'), case_name +'.csv')
df_list.to_csv(report_path, index = False, encoding = 'cp949')