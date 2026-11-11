CREATE TABLE sitemember (
	id varchar2(20char) PRIMARY KEY,
	pw varchar2(20char) NOT NULL,
	name varchar2(10char) NOT NULL,
	addr varchar2(100char) ,
	bday DATE ,
	tel varchar2(11char),
	photo varchar2(100char)
	);

SELECT * FROM sitemember;
SELECT count(*) FROM sitemember WHERE id = 'testid__';
SELECT * FROM sitemember WHERE id = 'testid__';

INSERT INTO sitemember values('testid__','testPW1@','test계정','12345!시군구!상세주소',to_date('20000202','yyyymmdd'),'','');


DELETE FROM sitemember;

DROP TABLE sitemember CASCADE CONSTRAINT purge;
--ㅇ.ㅇ.......