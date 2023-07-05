import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# SQL 문 실행 
c = conn.cursor()
c.execute('''SELECT ... FROM ... WHERE ... ''')

# 가져온 데이터를 파이썬에서 사용
rows = c.fetchall()
for row in rows:
    print(row)

# 연결 종료
conn.close()