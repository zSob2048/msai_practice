-- 프로젝트
--	조 구성
--	주제 선정
--	기능 분배
--	DB설계

-- testdata ; 홍길동, 수원사는, 19990101생, // 모나미153, 500, 문구류 판매
-- 판매자 탈퇴시 상품 삭제


CREATE SEQUENCE seller_1111_seq;
CREATE SEQUENCE product_1111_seq;


CREATE TABLE seller_1111(
	s_no number(3) PRIMARY KEY,
	s_name varchar2(8 char) NOT NULL  ,
	s_addr varchar2(8 char) NOT NULL  ,
	s_bday DATE NOT NULL);

INSERT INTO seller_1111 VALUES(0,'TEST','TEST',to_date('20000101','yyyymmdd'));
INSERT INTO seller_1111 VALUES(seller_1111_seq.nextval,'TEST23','T2ST2',to_date('20000101','yyyymmdd'));

CREATE TABLE product_1111(
	p_no number(4)	PRIMARY KEY,
	p_name varchar2(15 char) NOT NULL  ,
	p_price NUMBER(10) NOT NULL  ,
	p_cate varchar2(5 char) NOT NULL ,
	p_s_no NUMBER(3) NOT NULL,
	CONSTRAINT product_seller
		FOREIGN KEY (p_s_no) REFERENCES seller_1111(s_no)
		ON DELETE CASCADE	);

INSERT INTO product_1111 VALUES(0,'TEST',9999999999,'TEST',0);
INSERT INTO product_1111 VALUES(product_1111_seq.nextval,'TEST3',55555,'TEST',21);

SELECT * FROM seller_1111;
SELECT * FROM product_1111;


SELECT * FROM (
SELECT rownum AS rn, p_no, p_name, p_price, p_cate, s_name, s_addr, s_bday  FROM ( 
SELECT p_no, p_name, p_price, p_cate, s_name, s_addr, s_bday 
FROM seller_1111, product_1111 
WHERE s_no = p_s_no 
--AND (p_name LIKE '%s' OR p_cate LIKE '%s')
ORDER BY p_name, p_price 
) 
) 
WHERE rn >= 4 AND rn <= 6

SELECT p_no, p_name, p_price, p_cate, s_name, s_addr, s_bday FROM (
	SELECT * FROM ( 
		SELECT rownum AS rn, p_no, p_name, p_price, p_cate, p_s_no FROM ( 
			SELECT * FROM product_1111 WHERE p_name LIKE '%TE%' OR p_cate LIKE '%TE%' ORDER BY p_name, p_price ) ) 
		WHERE rn >= 4 AND rn <= 6
	),(
	SELECT *  FROM seller_1111 WHERE s_no IN ( 
		SELECT p_s_no FROM ( 
			SELECT rownum AS rn, p_no, p_name, p_price, p_cate, p_s_no FROM (
				SELECT * FROM product_1111 WHERE p_name LIKE '%TE%' OR p_cate LIKE '%TE%' ORDER BY p_name, p_price)) 
			WHERE rn >= 4 AND rn <= 6))
WHERE s_no = p_s_no ;
