import sqlite3

db = sqlite3.connect(':memory:')
sql = db.cursor()

sql.execute(""" CREATE TABLE сотрудники (
Id INT PRIMARY KEY, 
ФИО TEXT,
отдел TEXT,
моб тел INT
)""")

sql.execute(""" CREATE TABLE зарплата (
Id INT PRIMARY KEY, 
ФИО TEXT,
оклад BIGINT,
налог BIGINT,
FOREIGN KEY (Id) REFERENCES сотрудники (Id)
)""")

sql.execute(""" CREATE TABLE должность (
Id INT PRIMARY KEY, 
ФИО TEXT,
должность TEXT,
стаж NUMERIC,
FOREIGN KEY (Id) REFERENCES сотрудники (Id)
)""")
db.commit()

