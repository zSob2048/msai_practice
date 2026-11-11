# 프록시 client

# ai 엔드포인트 > 사용 > 유형 선택 수 카피페
# apikey 위치에 인증 기본키 카피페

# 테스트탭에서 
# > 
# {
#   "input data" : {
#       "columns" :  ["x","y"], # 넣어야하는 변수 명
#       "index"   : [0], # 결과값이 list 기준 몇번째 출력할지
#       "data"    : [[30,70], [10,20]] # 1개만 입력해도 2겹으로...
#   }
# }]

# >> 이 내용을 data 위치에 카피페

# 이후 json파싱..
# result 아래 파싱 
# result = json.loads(result)[0] 
# 추가


# 추후 AI클라이언트 부분에서 확인

# pip install azure-ai-ml
# pip install azure-identity


# Scikit-lear : 일반 AI 라이브러리
# 사용해서 만든걸
# MS환경에서 작업+모델등록+엔드포인트(=HTTP백엔드서버)

# MS환경에서 안하고 FastAPI로해도....

