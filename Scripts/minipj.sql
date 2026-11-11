CREATE SEQUENCE student_mpj_seq;

CREATE TABLE student_mpj(
	s_no number(3) PRIMARY KEY,
	s_name varchar2(5 char) NOT NULL,
	s_class varchar2(8 char) NOT NULL
);

INSERT INTO student_mpj values(0, 'TEST', 'TEST' );

SELECT * FROM student_mpj

----

--CREATE SEQUENCE test_mpj_seq;

CREATE TABLE test_correct_mpj(
	c_no number(3) PRIMARY KEY, -- 회차
	Q1 number(1) NOT NULL,
	Q2 number(1) NOT NULL,
	Q3 number(1) NOT NULL,
	Q4 number(1) NOT NULL,
	Q5 number(1) NOT NULL
);
INSERT INTO test_correct_mpj values(0,1,2,3,4,5);
INSERT INTO test_correct_mpj values(test_mpj_seq.nextval,2,5);

SELECT * FROM test_correct_mpj

----

CREATE TABLE test_score_mpj(
	t_c_no number(3) NOT NULL, 
	Q1 number(1) NOT NULL,
	Q2 number(1) NOT NULL,
	Q3 number(1) NOT NULL,
	Q4 number(1) NOT NULL,
	Q5 number(1) NOT NULL,
	
	t_s_no number(3) NOT NULL,
	t_score number(3) NOT NULL, 
	CONSTRAINT no_pk PRIMARY KEY(t_c_no, t_s_no),
	CONSTRAINT stdnum
		FOREIGN KEY (t_s_no) REFERENCES student_mpj(s_no)
		ON DELETE CASCADE 
);

INSERT INTO test_score_mpj values(0,1,2,3,4,5,0,100);

SELECT * FROM test_score_mpj

----

DELETE FROM test_score_mpj;
DROP TABLE test_correct_mpj CASCADE CONSTRAINT purge;
DROP TABLE test_score_mpj CASCADE CONSTRAINT purge;
