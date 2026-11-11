-- SQL

-- c s 	num+/- 글자크기
-- c a 	↑↓ 줄 복붙
-- c	d 줄 삭제
-- c	enter 실행 (커서위치의 문장 실행)
-- c	m 옆 화면

-- table 생성
CREATE TABLE test(
	name char,
	price int
);

-- 조회
SELECT  * FROM test;

------
-- DB관리자(x)
--	전원관리, 백업/복구, 사용자관리, ...
-- DBP
-- 	DB랑 연동되는 프로그램 개발
--	프로그램에서 발생한 데이터 DB에 저장하고...
--	데이터를 다루는 쪽에 집중
-- SQL
--	DB를 제어하는 언어
-- 언어는 어떤 DB를 쓰던 동일

-- sql의 경우 대/소문자 구별x (전부 대문자)
-- 우리는 데이터를 CRUD(Create Read Update Delete)하는정도

----

-- 새 파일 만들고 우클릭>Associate with data source

----

-- table
-- 	열(cloume), field
-- 	행(row), record, data
-- 테이블 완성

----

-- 테이블 만들기
-- CREATE TABLE 테이블명(
-- 	열제목 자료형 [옵션],
-- 	필드명 자료형 [옵션],
-- 	... -- 옵션 생략可
-- );
 
----

-- 자료형? >> OracleDB에만
-- 글자 		char(용량)     > 무조건 그 용량만큼 저장 (빈칸을 넣어서라도 용량에 맞게 저장)
--  		varchar2(용량) > 용량 조절, 용량을 조절하는 시간이 필요해 느림
-- '' 사용(큰따옴표 ㄴㄴ)
-- 수		number(n)   > 최대 n자리 정수
--  		number(n, m)> 전체 n자리, 소수점 아래 m자리 (= 정수부 n-m자리)
-- 날짜/시간	date

-- 파일? > 용량 개큼 > DB서버에 두면 DB서버>웹서버등 2번 이동해야됨 : 시간2배이벤트발생
-- ...

----

-- 용량
-- 5		: 5 bytes
-- 				> 숫자/영어 : 1byte
--		 		> 한글	  : 3bytes
-- 5 char	: 5글자 > 15 bytes

----

-- 테이블 생성
CREATE TABLE snack_1105(s_name varchar2(10 char), s_price number(6));
CREATE TABLE snack_1105(s_name varchar2(10 char) NOT NULL, s_price number(6) NOT NULL); -- 옵션 NOT NULL ; 공백ㄴㄴ
CREATE TABLE snack_1105(s_name varchar2(10 char) PRIMARY KEY, s_price number(6) NOT NULL); -- 옵션 PRIMARY KEY ; ~NULL + 중복불허 -- primary key 기준으로 데이터를 찾기 용이
-- auto increment : 자동 번호부여 옵션인데 여기 없음 >> SEQUENCE로 구현

----

-- SEQUENCE
-- CREATE SEQUENCE 시퀀스명;
CREATE SEQUENCE student_1105_seq; -- 보통 테이블명_seq로 명명
-- 이후 insert때 값 대신 사용(시퀀스명.nextval)
-- insert 실패해도 값은 올라감
DROP SEQUENCE student_1105_seq;

----

-- 테이블 삭제
-- DROP TABLE snack_1105; -- 까지만 해도 지워짐
DROP TABLE snack_1105 CASCADE CONSTRAINT purge; -- 오라클 자체 휴지통에 안남게 삭제

----

-- 데이터 넣기(C)
-- INSERT INTO 테이블명(필드명, 필드명, ...) values(값, 값, ...);
INSERT INTO snack_1105(s_name, s_price) values('초코파이', 5000);
INSERT INTO snack_1105(s_name, s_price) values('빼빼로', 1500);
INSERT INTO snack_1105(s_price, s_name) values(1800, '녹차빼빼로'); -- 순서 바뀌어도 가능
INSERT INTO snack_1105(s_name) values('오징어땅콩'); -- 일부 제외 가능 (안넣은건 NULL -> NOT NULL 옵션시 에러)
INSERT INTO snack_1105 values('아폴로', 300); -- 넣은 순서대로 가능(편리)
INSERT INTO snack_1105 values('포카칩', 1700);
INSERT INTO snack_1105 values('포카칩', 1800); -- PRIMARY KEY시 err

----

-- 조회
SELECT * FROM snack_1105;

----
CREATE TABLE student_1105(s_no NUMBER(2) PRIMARY KEY,
	s_name varchar2(3 char) NOT NULL, s_kor number(3) NOT NULL,
	s_eng number(3) NOT NULL,s_mat number(3) NOT NULL,
	s_bday DATE NOT NULL);
INSERT INTO student_1105 values(student_1105_seq.nextval,'홍길동', 100,80,90,sysdate); 
INSERT INTO student_1105 values(student_1105_seq.nextval,'김길동', 90,50,60, to_date('2000-04-15 05','yyyy-mm-dd hh24')); 
INSERT INTO student_1105 values(student_1105_seq.nextval,'홍길동', 0,10,5);
SELECT * FROM student_1105;
DROP TABLE student_1105 CASCADE CONSTRAINT purge;

----

-- DATE
-- sysdate : 현재시간날짜
-- to_date('값','패턴')
-- 	Y M D AM/PM HH(12시간제)/HH24 MI SS

------

CREATE TABLE snack2_1105 (
	s_num NUMBER(2) PRIMARY KEY ,
	s_name varchar2(10 char) NOT NULL, 
	s_enddate DATE NOT NULL,
	s_price NUMBER(5) NOT NULL ,
	s_mass NUMBER(5,2) NOT NULL );

CREATE SEQUENCE SNACK2_1105_SEQ;
DROP SEQUENCE SNACK2_1105_SEQ;

INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL,'초코파이', to_date('2025-12-01','YYYY-MM-DD') , 5000, 300.52 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '건빵',TO_DATE('2028-12-01','YYYY-MM-DD'),6000,180.52 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '포카칩',TO_DATE('2025-11-21','YYYY-MM-DD'),1700,150.31 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '포카칩',TO_DATE('2025-11-20','YYYY-MM-DD'),1700,150.31 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '새우깡',TO_DATE('2026-01-20','YYYY-MM-DD'),1800,130.03 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '쌀과자',TO_DATE('2027-01-20','YYYY-MM-DD'),2400,280.35 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '과자7',TO_DATE('2025-12-31','YYYY-MM-DD'),3300,420.77 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '과자8',TO_DATE('2026-03-10','YYYY-MM-DD'),400,30.03 );
INSERT INTO SNACK2_1105 values(SNACK2_1105_SEQ.NEXTVAL, '과자9',TO_DATE('2026-03-10','YYYY-MM-DD'),3400,430.03 );

SELECT * FROM SNACK2_1105;
DROP TABLE SNACK2_1105 CASCADE CONSTRAINT purge;


----

-- 데이터 조회 (R)
SELECT s_name, s_price FROM snack2_1105; -- 특정 필드만 조회
SELECT s_name AS name, s_price AS price FROM snack2_1105; -- 라벨 이름만 바꾸기
SELECT s_name , s_price/s_mass FROM snack2_1105; -- 연산자 사용 가능
SELECT s_name , s_price*0.1 AS vat FROM snack2_1105; -- 연산자 사용 가능

-- 통계 관련
-- sum avg max min count 등 有
SELECT avg(s_price) AS avgprice FROM snack2_1105;
SELECT max(s_price),min(s_price) FROM snack2_1105;
SELECT count(*) FROM snack2_1105; -- *: 분류전체 // 어차피 중복제거 안해줌

-- 특정 조건(데이터 필터링)
SELECT s_name, s_price FROM snack2_1105 WHERE s_price<=4000;
SELECT s_name, s_price FROM snack2_1105 WHERE s_name='포카칩';
SELECT s_name, s_price FROM snack2_1105 WHERE s_name like '%과자%';
SELECT s_name, s_price FROM snack2_1105 WHERE s_name like '%칩' OR s_name like '%깡';

-- 그룹별
SELECT s_name, avg(s_price) FROM snack2_1105 GROUP BY s_name;

-- 조건식(통계 결과값 필터링)
SELECT s_name, avg(s_price) FROM snack2_1105 GROUP BY s_name HAVING AVG(s_price)>=3000;

-- 정렬
SELECT s_name, s_price FROM snack2_1105 ORDER BY s_price; -- 기본 오름차순
SELECT s_name, s_price FROM snack2_1105 ORDER BY s_price desc; -- 내림차순
SELECT s_name, s_price FROM snack2_1105 ORDER BY s_price, s_name; -- 같은경우 다음 기준

-- rownum 이라는 select할때마다 부여되는 가상 필드가 존재(오라클에만~) 
-- 	*랑은 같이 못씀
--	order by 보다 먼저 부여됨 > from에 기존 select를 넣어서 최종 새로
--	1번부터만보여줌(왜죵) > 그냥 한번 더 씀
SELECT * 
FROM (
	SELECT rownum AS rn ,s_name, s_price 
	FROM(
		SELECT s_name, s_price FROM snack2_1105 ORDER BY s_price
		) 
	)
WHERE rn>=3 AND rn<=5;

-- 정렬 후 특정순번만 보여주세요...


----

-- 글자 이어붙이기
-- concat(STR, STR, ...)


SELECT s_name, s_enddate, s_price FROM SNACK2_1105 WHERE S_ENDDATE <= to_date( CONCAT(to_char( sysdate,'yyyymmdd'),'235959'), 'yyyymmdd hh24miss');

-- sysdate: 지금시간 >> 오늘 만 사용하려고...

-- TO_DATE (str,'YYDDMM') 	>> str→date
-- TO_CHAR (date,'YYDDMM')	>> date→str

to_char(,'yyyymmdd')
CONCAT(,'235959')
to_date( , 'yyyymmdd hh24miss')
-- >> 3개로 24시분초까지 붙이기
