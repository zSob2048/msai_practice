 -- 파일 직접업로드 ㄴㄴ / (파일경로+)파일명으로 저장 // 이름 길게(uuid 36자+기존파일명 >길어짐)
 
 CREATE TABLE post1219 (
 	m_id varchar2 (20 char) PRIMARY KEY ,
 	m_pw varchar2 (20 char) NOT NULL  ,
 	m_txt varchar2 (140 char) NOT NULL,  
 	m_img varchar2 (100 char) NOT NULL  ,
 	m_time DATE NOT NULL
 ); 
 
 SELECT * FROM post1219;
 
 SELECT count(*) FROM post1219;
 
 INSERT INTO post1219 values('aaaa','aaaa','aaaa','x.png',sysdate);
 
 --아오 하기싫어