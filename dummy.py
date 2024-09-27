import pyodbc
from faker import Faker

fake = Faker()

# Connect to SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=MUPELWA\\CSC4792;'
                      'DATABASE=Assignment_1;'
                      'UID=SA;'
                      'PWD=mupelwa2002;')

cursor = conn.cursor()

# Insert departments with explicit IDs
departments = [(1, 'Human Resources'), (2, 'Engineering'), (3, 'Finance')]
cursor.executemany("INSERT INTO Department (departmentID, department_name) VALUES (?, ?)", departments)

# Insert positions with department associations
positions = [(1, 'Manager', 1), (2, 'Technician', 2), (3, 'HR', 1)]  # Including positionID
cursor.executemany("INSERT INTO Positions (positionID, position_name, departmentID) VALUES (?, ?, ?)", positions)

# Dummy data insertion for staff
for i in range(1, 11):  # Generate 10 staff members with IDs 1-10
    name = fake.name()
    departmentID = fake.random_int(min=1, max=3)
    cursor.execute("INSERT INTO Staff (staffID, name, departmentID) VALUES (?, ?, ?)", (i, name, departmentID))
    
    # Insert into Staff_Position table
    positionID = fake.random_int(min=1, max=3)
    cursor.execute("INSERT INTO Staff_Position (staffID, positionID) VALUES (?, ?)", (i, positionID))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Dummy data inserted successfully!")