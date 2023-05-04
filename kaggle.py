import csv
import pymysql

titanic_db = pymysql.connect(
    host="localhost",
    user="titanic_user",
    password="titanic0000",
    db="titanic",
    charset="utf8",
)
db_cursor = titanic_db.cursor()
sql = """
INSERT
INTO
test (PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
VALUES (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)
"""
# VALUES (%d, %d, %s ,%s, %f, %d, %d, %s, %f, %s, %s)
# 테이블 스키마에 맞게 위와 같이 쓰니까 안됐음
f = open("test.csv", "r", encoding="utf-8")
csv_data = csv.reader(f)
for line in csv_data:
    # 첫 번째 라인은 필드명이기 때문에 건너뛰는 작업
    if line[0] == "PassengerId":
        continue

    # 자꾸 에러가 나서 각 항목에 대해 빈 항목이 있는 경우를 일일히 처리해주었다.
    PassengerId = int(line[0]) if line[0] != "" else None
    Pclass = int(line[1]) if line[1] != "" else None
    Name = line[2] if line[2] != "" else None
    Sex = line[3]
    Age = float(line[4]) if line[4] != "" else None
    SibSp = int(line[5]) if line[5] != "" else None
    Parch = int(line[6]) if line[6] != "" else None
    Ticket = line[7]
    Fare = float(line[8]) if line[8] != "" else None
    Cabin = line[9]
    Embarked = line[10]

    # 아래의 명령어가 실행되려면 빈 항목에 대한 처리가 필요했다.
    db_cursor.execute(
        sql,
        (
            PassengerId,
            Pclass,
            Name,
            Sex,
            Age,
            SibSp,
            Parch,
            Ticket,
            Fare,
            Cabin,
            Embarked,
        ),
    )

titanic_db.commit()
titanic_db.close()
f.close()
