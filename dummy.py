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

# Insert positions and departments with correct foreign key references
departments = [('Human Resources',), ('Engineering',), ('Finance',)]
cursor.executemany("INSERT INTO Departments (department_name) VALUES (?)", departments)

# Make sure to associate each position with a department
positions = [('Manager', 1), ('Technician', 2), ('HR', 1)]  # Assuming department 1 for HR, 2 for Engineering, etc.
cursor.executemany("INSERT INTO Positions (position_name, departmentID) VALUES (?, ?)", positions)

# Dummy data insertion for staff
for _ in range(10):
    name = fake.name()
    departmentID = fake.random_int(min=1, max=3)  # Ensure the department matches the available IDs
    cursor.execute("INSERT INTO Staff (name, departmentID) VALUES (?, ?)", (name, departmentID))

    # Get the last inserted staff member's ID
    staffID = cursor.execute("SELECT @@IDENTITY AS id").fetchval()

    # Now, insert the many-to-many relationship in the Staff_Position table
    positionID = fake.random_int(min=1, max=3)  # Random position assignment
    cursor.execute("INSERT INTO Staff_Position (staffID, positionID) VALUES (?, ?)", (staffID, positionID))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Dummy data inserted successfully!")
