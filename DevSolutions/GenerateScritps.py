from faker import Faker 
import random 
import datetime 
import pyodbc  # For MS SQL Server connections

fake = Faker() 

# Database Connection Details (Replace with your own)
server = 'KIRKPC\SALEMSERVER'
database = 'dbDevSolutions'
driver = '{ODBC Driver 17 for SQL Server}'  
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Define lists to store generated IDs 
employee_ids = []
address_ids = []

# Function to generate a random date of birth
def generate_dob():
    return fake.date_of_birth(minimum_age=18, maximum_age=90)


def generate_audit_log_records(num_records):
    with pyodbc.connect(conn_str) as conn, conn.cursor() as cursor:
       cursor.execute("-- Audit Log Table\n")
       cursor.execute("INSERT INTO tblAuditLog (audTableName, audRecordId, audActionType, audActionDescription, audUsrIdfk, audActionDate) VALUES (?, ?, ?, ?, ?, ?)", 
                   [fake.word(), random.randint(1, 1000), fake.random_element(['INSERT', 'UPDATE', 'DELETE']), fake.sentence(),  random.choice(employee_ids), datetime.datetime.now()] * num_records)  # Adjust based on your data

def generate_address_records(num_records):
    with pyodbc.connect(conn_str) as conn, conn.cursor() as cursor:
        cursor.execute("-- Address Table\n")
        cursor.execute("INSERT INTO tblGenAddress (adrTwnIdfk, adrRgnIdfk, adrCtyIdfk, adrAdtIdfk, adrStreet, adrZipcode, adrDescription, adrCreatedDate, adrLastEditDate, adrCreatedByUsrIdfk, adrEditedByUsrIdfk) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                   [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 5), fake.street_address(), fake.zipcode(), fake.sentence(nb_words=6), datetime.datetime.now(),datetime.datetime.now(), 1, 1 ] * num_records)  # Adjust foreign key ranges
        cursor.execute("SELECT adrIdpk FROM tblGenAddress") 
        address_ids.extend([row[0] for row in cursor.fetchall()])  # Store generated Address IDs

def generate_employee_records(num_records):
    with pyodbc.connect(conn_str) as conn, conn.cursor() as cursor:
        cursor.execute("-- Employee Table\n")
        cursor.execute("INSERT INTO tblHrEmployees (empStaffNo, empLastName, empOtherName, empFirstName, empDoB, empRecriutmentDate, empMobileNo, empEmail, empTltIdfk, empAdrIdfk, empGndIdfk, empJbtIdfk, empCreationDate, empLastEditDate, empCreatedByUsrIdfk, empEditedByUsrIdfk) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   [random.randint(1000, 9999), fake.last_name(), fake.first_name(), fake.first_name(), generate_dob(), datetime.datetime.now().date(), fake.phone_number(), fake.email(), random.randint(1, 5), random.choice(address_ids), random.randint(1, 2), random.randint(1, 5), datetime.datetime.now(), datetime.datetime.now(), 1,1] * num_records) 
        cursor.execute("SELECT empIdpk FROM tblHrEmployees") 
        employee_ids.extend([row[0] for row in cursor.fetchall()])  # Store the generated Employee IDs


# ADJUSTED: Number of Records to Generate Based on Your Requirements 

num_audit_log_records = 500 
num_addresses = 200
num_employees = 100

# ADJUSTMENT: Call Your Specific Functions in the Correct Order Based on Foreign Key Dependencies 

generate_address_records(num_addresses) # Generate addresses
generate_employee_records(num_employees)  # Generate employees 

generate_audit_log_records(num_audit_log_records) # Example: Generate audit log data

