import faker
import pyodbc


fake = faker.Faker()  

def connect_database():
    server = 'KIRKPC\SALEMSERVER'
    database = 'dbDevSolutions'
    username = ''
    password = '' 
    driver = '{ODBC Driver 17 for SQL Server}' 

    conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(conn_str)


def generate_employee():
    name = fake.name().split(" ")
    email = name[0].lower() + "." + name[1].lower() + "@africoda.com"
    job_title = fake.job()
    # ... other employee fields
    return name[0], name[1], email, job_title

def generate_task(project_ids):
    task_name = fake.sentence(nb_words=4) 
    description = fake.paragraph()
    assignee_id = fake.random_element(elements=range(1,4 ))  # Assuming you have 20 employees 
    project_id = fake.random_element(elements=project_ids)
    # ... other task fields
    return task_name, description, assignee_id, project_id 

def insert_data(connection, table_name, data):
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor = connection.cursor()
    cursor.execute(sql, tuple(data.values()))
    connection.commit()

if __name__ == '__main__':
    connection = connect_database()

    # Generate and insert employees
    for _ in range(20):
        employee_data = generate_employee()
        insert_data(connection, 'tblHrEmployees', employee_data)



    connection.close()
