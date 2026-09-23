# DB 연결 및 커넥션 생성
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. 접속 정보 준비
id = 'web_user'
pw = 'user@pass'
host = '54.252.215.90'
port = 3306
database = 'mydb'
url = f'mysql+pymysql://{id}:{pw}@{host}:{port}/{database}'

# 2. 엔진 생성
#echo=True : 내가 전송하는 쿼리 로그 출력
engine = create_engine(url=url,echo=True)

# 3. 세션 준비
session = sessionmaker(bind=engine)

# 4. 세션을 사용자에게 전달
def get_conn():
    return session() # 이 함수를 실행하면 커넥션을 뱉어낸다.

"""
CREATE TABLE member(
    id VARCHAR(50) PRIMARY KEY,
    pw VARCHAR(100),
    name VARCHAR(20),
    age INT(3),
    gender VARCHAR(4),
    email VARCHAR(50)
);

SELECT COUNT(id) AS cnt FROM member WHERE id = 'admin';
"""