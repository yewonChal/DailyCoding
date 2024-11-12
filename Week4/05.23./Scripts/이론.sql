-- SQL SELECT 문 : 데이터베이스에서 정보를 검색하는데 사용되는 코드

-- 1) SELECT 절 : SELECT문의 시작을 담당한다. 어떤 열을 반환할건지 지정한다. SELECT* = 모든 열
-- 2) FROM 절 : 어떤 테이블에서 데이터를 검색할 것인지 지정한다. 마지막을 담당
-- 3) WHERE 절 : 특정 조건을 만족하는 행을 선택하도록 필터링한다.
-- 4) ORDER BY 절 : 정렬 순서를 지정한다.
-- 5) GROUP BY 절 : 특정 열에 따라서 그룹화한다.
-- 6) HAVING 절 : GROUP BY의 친구(함께 사용해야한다.) GROUP BY에서 추가 필터링을 도와준다.

-- SELECT절
-- SELECT COLUMN1, COLUMN2, COLUMN3, ... ,COLUMNN 이와같이 직접 지정해서 데이터 열기 가능
-- column : 반환하고자 하는 테이블 열의 이름

-- FROM절
-- FROM table1, table2, table3, ..., tableN 
-- 해당 table 내에서 데이터를 검색하고자 한다.

-- SELECT table1.column1, table2.column2 -> 테이블은 객체가 맞구나
-- FROM table1, table2;

-- DISTINCT 키워드
-- 중복된 결과를 제거하고 고유한 결과만을 반환하는데 사용된다.
-- SELECT절에서 column 앞에 작성한다.
-- SELECT DISTINCT column

-- WHERE절
-- 필터링 -> 조건식 -> 만족하는 행만이 결과에 포함된다.
-- SELECT column1, column2, ..., columnN
-- FROM table
-- WHERE 조건식;

-- # people 테이블에서 나아가 30 초과 50 미만인 사람들을 필터링하겠다.DEPT
-- SELECT*
-- FROM people
-- WHERE age > 30 AND age < 50;

-- ORDER BY 절
-- 특정 열 또는 여러 열에 따라서 정렬해준다.
-- 기본적으로 오름차순(ASC), 내림차순(DESC)으로 정렬하려면 DESC 키워드를 사용해야 한다.

-- SELECT column1, column2, ...
-- FROM table
-- ORDER BY column1 ASC, column2 DESC 

-- # 직원 이름 순서대로 정렬해서 부서 코드랑 같이 출력
-- SELECT ENAME, empno
-- FROM EMP 
-- ORDER BY ename 

-- GROUP BY절 
-- 보통 집계함수와 함께 사용되어 그룹화해주거나 계산해주는데 사용된다.

-- SELECT column1, column2, ..., function(columnN) 
-- FROM table  
-- GROUP BY column1, column2. 

-- # 테이블에서 각 empno, name의 평균 급여를 계산. 
-- SELECT empno, name, AVG(salary)
-- FROM table
-- GROUP BY empno, name

-- 비교연산자 <, >, <=, >=, =, !=

-- BETWEEN ... AND ... : 특정 범위 
-- 1 < a < 100 -> WHERE a BETWEEN 1 AND 100

-- IN -> WHERE a IN('개발', '본부', '디자인')

-- LIKE : 문자열 패턴 매칭 _, %와 같이 사용한다.
-- %는 임의의 문자열을 대체하고, _는 임의의 한 개의 문자를 대체한다.
-- _A% : 두 번째 글자가 A인 모든 값
-- WHERE name LIKE _A% 

-- IS NULL, IS NOT NULL : NULL인지 아닌지 판단

-- HAVING절 : GROUP BY 추가 필터링

-- SELECT column1, column2, ..., function(columnN)
-- FROM table
-- GROUP BY column1, column2
-- HAVING condition;

-- # 부서별, 직급별로 평균 급여를 계산 그 중 3000 이하인 애들만 조회
-- SELECT DEPTNO, JOB, AVG(DAL)
-- FROM EMP
-- WHERE AVG(SAL) < 3000;

-- 연산 기법
-- 1) 셀렉션 : 특정 조건을 만족하는 행을 선택하겠다. WHERE
-- 2) 프로젝션 : 특정 열만 선택하는 연산. SELECT
-- 3) 조인 : 여러 개의 테이블에서 관련있는 데이터를 결합하는 연산. JOIN ... ON

-- SELECT ENAME, EMPNO, DNAME, LOC
-- FROM EMP
-- JOIN DEPT ON EMP.DEPTNO == DEPT.DEPTNO
