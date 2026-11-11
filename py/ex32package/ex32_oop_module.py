# Python > module(.py) > class : 라서 그냥 객체지향 하기실흐면 안해드 댐
# Java > class : 얜 객체지향 해야댐

# 남의 작업 가져다 쓰자... > 이름 중복?
# : package(필수x) > module(.py) > class 라서 package로 해결하기...
# package까지 중복되면?? > 좀 신경써서 중복안되게 지어라... 가 java이야기 (보통 com.회사명.프로젝트명.주제 식으로 다 때려박음)
# python : 해당 부분 추후 확인

# vscode > Python 용어랑 약간씩 차이가 있음...
# >> 패키지 만들고싶어요!! >> 그냥 폴더를 만들고 그 안에 __init__.py (뭐 적을필요 X)

# # import :외부파일에서 불러오려면...
# # 방법 3가지
# import animal.pet # import 패키지명.모듈명.클래스명...
# d = animal.pet.dog()

# import animal.pet as ap # import 패키지명.모듈명 as 별칭 >> 이후 짧게 쓸 수 있음
# d = ap.dog()

# from animal.pet import dog # from 패키지명.모듈명 import 가져올거


from random import randint


randint(3,10) # > 자동완성시 3번st로 해줌~ (vs코드에서

# 3번 스타일을 주로 쓰지만... 1, 2도 써야함(중복된다거나...)
# 설정한게 나오긴 함(파일에)

# Win에서 PYTHONPATH를 설정하면 프로젝트도 패키지처럼 인식해서...
# >> 실시간 데이터 받아와서 저장 뭐 이런... (윈도우 환경, 리눅스는 추후 진행)

####################################

