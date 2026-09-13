
import psycopg2
import glob

filename = glob.glob('raw/employee_data_*.csv')

conn = psycopg2.connect(
    host="localhost",
    database="healthcare_workforce_pipeline",
    user="postgres",
    password="Maleek11",
    port=5432
)

cur = conn.cursor()

try:
    # Create schema
    cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")

    # Drop existing tables if they exist
    cur.execute("""
    DROP TABLE IF EXISTS
        raw.employees
""")

    # Create tables inside the raw schema
    cur.execute("""
    CREATE TABLE raw.employees(
    emp_id VARCHAR(100) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    dob DATE,
    telephone VARCHAR(100),
    address VARCHAR(200),
    gender VARCHAR(100),
    trust VARCHAR(100),
    ethnicity VARCHAR(100),
    nationality VARCHAR(100),
    visa_status VARCHAR(100),
    staff_group VARCHAR(100),
    role VARCHAR(100),
    division VARCHAR(100),
    grade VARCHAR(100),
    salary NUMERIC,
    hire_date DATE,
    contract_start DATE,
    weekly_hours NUMERIC,
    fte NUMERIC,
    registration_type VARCHAR(100),
    contract_type VARCHAR(100),
    employment_status VARCHAR(100),
    registration_no VARCHAR(100),
    registration_expiry_date DATE,
    ni VARCHAR(100),
    dbs_expiry_date DATE,
    mandatory_training_expiry_date DATE,
    profile_creation_date DATE
    )
""")

    # Load data into schema tables
    for files in filename:
        with open(files, 'r') as f:
            next(f)
            cur.copy_expert("COPY raw.employees FROM STDIN WITH CSV", f)

    conn.commit()

except Exception as e:
    print("Error: ",e)
    conn.rollback()

finally:
    cur.close()
    conn.close()