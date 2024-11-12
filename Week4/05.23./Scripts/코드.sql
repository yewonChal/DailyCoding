CREATE TABLE book_list ( -- 테이블 생성
	book_no		varchar(16) not null, -- book_no 조건 생성, varchar, 16자로 형식 고정, no null = 데이터가 필수로 존재
	book_name	varchar(50), -- 유연하게 설정하고 싶다면, not null을 생략해도 괜찮다.
	writer		varchar(50),
	publisher	varchar(30),
	reg_date	date, -- date : 날짜형식
	price		int
)

use mysql; -- mysq를 활용하여 생성

SELECT * FROM book_info; -- book_list 테이블 추출(이름 변경 후 book_info)

INSERT INTO book_info values('1202888600046538','Bigdata','Maickop','EDItion','20220923',21000); -- 데이터값 입력