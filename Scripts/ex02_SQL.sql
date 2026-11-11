-- DBMS 분류중...
-- 	Relational DBMS(RDBMS, 관계형DB) : 테이블을 나눠서 설계, 테이블 간 관계 중심... (> Oracle MySQL etc)
-- 테이블간 관계 > 1: N // M: N
-- 1:N > N쪽 테이블에 1쪽 테이블 PK에 해당하는 필드 추가
-- M:N > 두 테이블의 PK들이 있는 테이블 하나 따로 생성
--  NoSQL : MongoDB etc...




CREATE SEQUENCE run_1106_seq;

CREATE TABLE run_1106(
	r_no NUMBER(2) PRIMARY KEY , 
	r_c_no NUMBER(2) NOT NULL  ,
	r_r_no NUMBER(2) NOT NULL  
);

INSERT INTO run_1106 values(run_1106_seq.nextval, 1, 1);
INSERT INTO run_1106 values(run_1106_seq.nextval, 1, 2);
INSERT INTO run_1106 values(run_1106_seq.nextval, 2, 1);

----

CREATE SEQUENCE ceo_1106_seq;

CREATE TABLE ceo_1106(
	c_no NUMBER(2) PRIMARY KEY , 
	c_name varchar2(5 char) NOT NULL  ,
	c_bday DATE NOT NULL,
	c_addr varchar2(8 char) NOT NULL    
);

INSERT INTO ceo_1106 values(ceo_1106_seq.nextval, '홍길동', to_date('1999-01-01','yyyy-mm-dd'), '수원');
INSERT INTO ceo_1106 values(ceo_1106_seq.nextval, '김길동', to_date('2000-03-03','yyyy-mm-dd'), '안양');

----

CREATE SEQUENCE restaurant_1106_seq;

CREATE TABLE restaurant_1106(
	r_no NUMBER(2) PRIMARY KEY , 
	r_name varchar2(8 char) NOT NULL  ,
	r_jijum varchar2(8 char) NOT NULL,
	t_table NUMBER(3) NOT NULL  
);

INSERT INTO restaurant_1106 values(restaurant_1106_seq.nextval,'김밥천국', '종로', 10);
INSERT INTO restaurant_1106 values(restaurant_1106_seq.nextval,'김밥천국', '서초', 20);
INSERT INTO restaurant_1106 values(restaurant_1106_seq.nextval,'우동천국', '종로', 15);

----

CREATE SEQUENCE menu_1106_seq;

CREATE TABLE menu_1106(
	m_no NUMBER(2) PRIMARY KEY , 
	m_name varchar2(8 char) NOT NULL  ,
	m_price NUMBER(7) NOT NULL  ,
	m_cate varchar2(5 char) NOT NULL ,
	m_r_no NUMBER(2) NOT NULL  
);

INSERT INTO menu_1106 values(menu_1106_seq.nextval,'야채김밥', 4000, '식사', 1);
INSERT INTO menu_1106 values(menu_1106_seq.nextval,'비빔밥'	, 5000, '식사', 2);
INSERT INTO menu_1106 values(menu_1106_seq.nextval,'우동'	, 4500, '식사', 3);
INSERT INTO menu_1106 values(menu_1106_seq.nextval,'비빔밥'	, 5500, '식사', 3);
INSERT INTO menu_1106 values(menu_1106_seq.nextval,'카스'	, 6000, '술	', 1);

----

SELECT * FROM run_1106;
SELECT * FROM ceo_1106;
SELECT * FROM restaurant_1106;
SELECT * FROM menu_1106;


----

-- 최연장자 사장 이름
SELECT c_name FROM ceo_1106 WHERE c_bday = (SELECT min(c_bday) FROM ceo_1106)

-- 밥 시리즈 최고가
SELECT max(m_price) FROM menu_1106 WHERE m_name LIKE '%밥%'

-- 김밥천국 종로점의 메뉴/가격
SELECT m_name FROM menu_1106 WHERE m_no = (SELECT r_no FROM restaurant_1106 WHERE r_name = '김밥천국' AND r_jijum = '종로');

-- subquery로 나오는 결과가 여러개일 수 있는 경우 >> = 대신 in 으로

-- 전체 ; 테이블이 나눠져 있는 경우
SELECT * FROM restaurant_1106 , menu_1106 WHERE r_no = m_r_no; -- join: 테이블 붙이기, 전체 경우의 수를 보여줌 >> where로 조정
-- 필드명이 겹치는 경우 > table.으로 정의
SELECT * FROM restaurant_1106 , run_1106 ,ceo_1106 WHERE r_c_no= c_no AND r_r_no = restaurant_1106.r_no;

-- join의 경우 data가 ㅈㄴ많아짐 미친색이임ㅋㅋ 하지마샘
-- >> 무조건 한꺼번에 봐야만 할때 join 이외엔 ㄴㄴ

SELECT rownum, m_name, m_price FROM (SELECT m_name, m_price FROM menu_1106 ORDER BY m_name);

----

-- foreign key (외래키)
-- 1) 정확한 번호만 가능하도록...(인덱스#)
-- 2) 다른 테이블에서 삭제된 경우...(자동 삭제)

-- constraint 제약조건
-- 		foreign key (필드명) references 테이블명(필드명)
-- 		on delete cascade
CREATE TABLE menu_1106(
	m_no NUMBER(2) PRIMARY KEY , 
	m_name varchar2(8 char) NOT NULL  ,
	m_price NUMBER(7) NOT NULL  ,
	m_cate varchar2(5 char) NOT NULL ,
	m_r_no NUMBER(2) NOT NULL  
	CONSTRAINT menu_restaurant -- 이건 그냥 이름(아무거나?)
		FOREIGN KEY (m_r_no) REFERENCES restaurant_1107(r_no)
		ON DELETE CASCADE 
);







