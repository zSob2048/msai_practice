
CREATE TABLE seoul_dust( 
	sd_date date NOT NULL, 
	sd_msrrgn_nm char(3 char) NOT NULL, 
	sd_msrste_nm varchar2 (4 char) NOT NULL,
	sd_pm10 number(3) NOT NULL,
	sd_pm25 number(3) NOT NULL,
	sd_idex_nm varchar2 (10 char) NOT NULL
);

-- primary key > db중 원하는 정보를 찍는게 중요한 경우...
-- BD / AI학습분야에는 굳이?

SELECT * FROM seoul_dust;

 