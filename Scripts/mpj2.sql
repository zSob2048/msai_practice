CREATE SEQUENCE company_1203_seq;
CREATE SEQUENCE product_1203_seq;

CREATE TABLE company_1203(
	c_no number(5) PRIMARY KEY , 
	c_ceo varchar(5 char) NOT NULL  ,
	c_loc varchar(5 char) NOT NULL  ,
	c_bday DATE NOT NULL  
);

INSERT INTO company_1203 values(company_1203_seq.nextval,  '홍길동','강남',to_date('19990101','yyyymmdd'));
INSERT INTO company_1203 values(company_1203_seq.nextval,  '소길동','주소',to_date('19990101','yyyymmdd'));

CREATE TABLE product_1203(
	p_no number(5) PRIMARY KEY , 
	p_name varchar(10 char) NOT NULL , 
	p_price number(6) NOT NULL  ,
	p_stock number(6) NOT NULL  ,
	p_c_no number(5) NOT NULL  ,
		CONSTRAINT comp_prod
		FOREIGN KEY (p_c_no) REFERENCES company_1203(c_no)
		ON DELETE CASCADE 
);

INSERT INTO product_1203 values(product_1203_seq.nextval,  '모나미156', 500,10,84);

SELECT * FROM company_1203;
SELECT * FROM product_1203;

DROP TABLE company_1203 CASCADE CONSTRAINT purge;
DROP TABLE product_1203 CASCADE CONSTRAINT purge;

---------------------------------------------------------------------------------------

CREATE SEQUENCE memo1203_seq;

CREATE TABLE mainmemo1203(
	m_no number(5) PRIMARY KEY , 
	m_content varchar2(1000 char) NOT NULL  ,
	m_correct NUMBER(2) NOT NULL,
	m_uplodedate DATE NOT NULL  
);

CREATE TABLE replymemo1203(
	r_no number(5) PRIMARY KEY , 
	r_m_no number(5) NOT NULL,
	r_content varchar2(1000 char) NOT NULL  ,
	r_uplodedate DATE NOT NULL,
		CONSTRAINT replymemo
		FOREIGN KEY (r_m_no) REFERENCES mainmemo1203(m_no)
		ON DELETE CASCADE 
);

SELECT * FROM MAINMEMO1203;
SELECT * FROM REPLYMEMO1203;


INSERT INTO MAINMEMO1203 values(0,  '내용은 1000자까지 입력 가능', 0, to_date('20000101','yyyymmdd'));
INSERT INTO REPLYMEMO1203 values(0, 0, '답글도 1000자까지 입력 가능, 수정할 수 없습니다.', to_date('20000101','yyyymmdd'));

DROP TABLE MAINMEMO1203 CASCADE CONSTRAINT purge;
DROP TABLE REPLYMEMO1203 CASCADE CONSTRAINT purge;