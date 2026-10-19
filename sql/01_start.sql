SELECT * FROM mysql.user;

# 주석 
-- 주석(대표주석)

# database 확인 - 테이블을 모아놓은 저장소
SHOW databases;

# CREATE 로 만든 녀석은 대부분 DROP 으로 삭제되고 ALTER 로 수정된다.
-- CREATE DATABASE [이름]; 	<- 만들기
-- DROP DATABASE [이름];		<- 삭제
-- USE [테이터베이스 이름];		<- 사용(들어가기)

-- mydb 라는 database 만들어보기, 그리고 사용하기
CREATE DATABASE mydb;
USE mydb;

-- 테이블 확인
SHOW tables;

-- 테이블 생성
/*
CREATE TABLE [테이블명](
	[컬럼명] [데이터타입](사이즈),
	...
);
*/
/*1) 문자타입
 * 고정형 CHAR(바이트)
 * 가변경 VARCHAR(바이트) -> 바이트 크기만큼 자리잡았다가 데이터가 작으면 줄어든다.
 * TEXT: 65MB
 * LONGTEXT 4GB
 * */
/*2) 숫자타입
 * INT, FLOAT, BIGINT, DOUBLE
 * */
/*3) BOOLEAN -> 0,1*/
/*4) 날짜타입
 * DATE		: 0000-00-00
 * DATETIME	: 0000-00-00 00:00:00.000
 * TIMESTAMP: DATETIME 과 같지만 time-zone에 따라 시간이 변경된다.
 * */

CREATE TABLE test_table(
	user_name VARCHAR(40),
	age INT(3),
	mobile VARCHAR(20),
	reg_date DATE DEFAULT CURDATE()
);

-- 테이블 구조 확인
DESC test_table;

-- 테이블을 아래와 같이 만들어 보자
-- 테이블 명 : employees
-- emp_no 숫자형 3자리
-- first_name 문자열 8자
-- last_name 문자열 2자
-- email 문자열 50자
-- mobile 문자열 11자
-- salary 숫자형 8자
-- reg_date 날짜 기본으로 입력 된다.
CREATE TABLE employees(
	emp_no INT(3),
	first_name VARCHAR(8),
	last_name VARCHAR(8),
	email VARCHAR(50),
	mobile VARCHAR(11),
	salary INT(8),
	reg_date DATE DEFAULT CURDATE()
);
desc employees; -- 테이블 구조 확인
-- database 내 테이블 목록
show tables;

-- 테이블 삭제
DROP TABLE test_table;

-- 테이블 수정
-- 1) 컬럼 이름 수정
-- ALTER TALBE [테이블 이름] RENAME COLUMN [변경전이름] TO [변경 후 이름]
ALTER TABLE employees RENAME COLUMN last_name TO family_name;
DESC employees;

-- 2) 컬럼 추가
-- ALTER TALBE [테이블이름] ADD ([컬럼명] [데이터타입](사이즈));
ALTER TABLE employees ADD (depart_no VARCHAR(10));
ALTER TABLE employees ADD (commission VARCHAR(10));
ALTER TABLE employees ADD (etc VARCHAR(100));
DESC employees;

-- 3) 컬럼 속성 변경
-- ALTER TABLE [테이블이름] MODIFY COLUMN [컬럼명] [데이터타입](사이즈);
-- 00.00 의 경우 float(전체자리수,소숫점자리수)
ALTER TABLE employees MODIFY COLUMN commission float(4,2);
DESC employees;

-- 4) 컬럼 삭제
-- ALTER TABLE [테이블명] DROP COLUMN [컬럼명];
-- etc 컬럼 삭제
ALTER TABLE employees DROP COLUMN etc;
































