CREATE SEQUENCE snack_1107_seq;

-- DB서버...> HDD

CREATE TABLE company_1107(
	c_name varchar(5 char) PRIMARY KEY , 
	c_add varchar(10 char) NOT NULL  ,
	c_ceo varchar(10 char) NOT NULL  ,
	c_emp NUMBER(5) NOT NULL  
);

INSERT INTO company_1107 values('오리온', '강남', '홍길동',100);
INSERT INTO company_1107 values('롯데', '인천', '김길동',200);
INSERT INTO company_1107 values('크라운', '안양', '홍길동',50);

---


CREATE TABLE snack_1107(
	s_no NUMBER(2) PRIMARY KEY , 
	s_name varchar(10 char) NOT NULL  ,
	s_price NUMBER(6) NOT NULL  ,
	s_mass NUMBER(6,2) NOT NULL  ,
	s_exp DATE NOT NULL  ,
	s_c_name varchar(5 char) NOT NULL  
);

INSERT INTO snack_1107 values(snack_1107_seq.nextval,'초코파이', 5000,500.23,to_date('2025-11-08','yyyy-mm-dd'),'오리온');
INSERT INTO snack_1107 values(snack_1107_seq.nextval,'초코파이', 5000,500.23,to_date('20251118','yyyymmdd'),'오리온');
INSERT INTO snack_1107 values(snack_1107_seq.nextval,'롯데샌드', 3000,200.12,to_date('20251201','yyyymmdd'),'롯데');
INSERT INTO snack_1107 values(snack_1107_seq.nextval,'초코파이', 4800,450.88,to_date('20251218','yyyymmdd'),'롯데');
INSERT INTO snack_1107 values(snack_1107_seq.nextval,'과자1', 1700,230.48,to_date('20260103','yyyymmdd'),'크라운');
INSERT INTO snack_1107 values(snack_1107_seq.nextval,'과자2', 2700,180.33,to_date('20251129','yyyymmdd'),'크라운');

SELECT * FROM company_1107;
SELECT * FROM snack_1107;

--

-- 출력결과상의 중복 제거
SELECT DISTINCT s_name, s_price FROM snack_1107;

-- 회사별-이름별 재고
SELECT s_c_name, s_name, count(*) FROM snack_1107 GROUP BY s_c_name, s_name;
SELECT count(*) FROM snack_1107;

----

-- U pdate
UPDATE company_1107 SET c_emp = 50 WHERE c_name = '오리온';
-- where이 없어도 작동(이 경우 테이블 전체가 변경됨)
UPDATE snack_1107 SET s_price = s_price + 500 WHERE s_name LIKE  '%초코%'; -- 수식 가능

-- D elete
DELETE FROM snack_1107 WHERE s_name = '롯데샌드';
