# Phase 1
# extract-highschool.py
# 고등학교만 추출해보자

import pandas as pd

file_path = 'data/origin.xlsx'

data = pd.read_excel(file_path) 

# 학제, 시도, 학교명, 홈페이지면 필요한 정보는 모두 있는 것 같다. 
df = data.loc[:, ['학제', '시도', '학교명', '홈페이지']]

# 학제가 고등학교인 행만 추출
df_highschools = df[df['학제'] == '고등학교']

# 추출했으니 학제도 이제 필요없다. 
df_result = df_highschools.loc[:, ['시도', '학교명', '홈페이지']]

# excel 로 뽑아보자
df_result.to_excel('data/highschool-extracted.xlsx', sheet_name = 'Sheet1')