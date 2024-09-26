import pyodbc
from faker import Faker

fake = Faker()

conn = pyodbc.connect('DRIVER={SQL Server};'
                    'SERVER=MUPELWA\CSC4792 ;'
                    'DATABASE =Assignment_1;'
                    'UID=SA'
                    'PWD =mupelwa2002;')

cursor = conn.cursor()

positions = [('Manager',), ('Technician',), ('HR',)]
cursor.executemany("INSERT Positions (position_name) VALUES(?)", positions)

departments = [('Human Resources',),('Engineering',),('Finance',)]
cursor.executemany("INSERT INTO departments (department_name) VALUES(?)", departments)

#dummy data insertion
for _ in range(10):
    name = fake.name()
    positionID = fake.random_int(min=1, max=3)
    departmentID = fake.random_int(min=1, max=3)
    cursor.execute("INSERT INTO Staff (name, positionID, departmentID) VALUES(?,?,?)", (name, positionID, departmentID))
    
conn.commit()

cursor.close()
conn.close()

print("Dummy data inserted successfully!")