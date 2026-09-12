import random
import pandas as pd
from faker import Faker
from datetime import datetime
from dateutil.relativedelta import relativedelta
from variable import trust_name

faker = Faker("en_GB")

filename_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

NUMBER_OF_EMPLOYEES = 1200

"""
Reference Data
"""

staff_groups = {
    "Nursing": [
        "Healthcare Assistant",
        "Staff Nurse",
        "Senior Staff Nurse",
        "Charge Nurse",
        "Ward Manager",
        "Nursery Nurse"
    ],
    "Medical": [
        "FY1/FY2",
        "SHO",
        "Registrar",
        "Consultant",
        "GP"
    ],
    "AHP": [
        "Physiotherapist",
        "Occupational Therapist",
        "Radiographer",
        "Speech Therapist",
        "Pharmacist",
        "Physiologist"
    ],
    "Admin": [
        "Administrator",
        "Receptionist",
        "Medical Secretary",
        "Data Analyst"
    ]
}

divisions = {
    "Medicine & Acute Care": [
        "Acute Medicine",
        "Cardiology",
        "Dermatology",
        "Endocrinology",
        "Gastroenterology",
        "General Surgery",
        "Geriatrics",
        "Haematology",
        "Infectious Diseases",
        "Nephrology",
        "Neurology",
        "Oncology",
        "Respiratory Medicine",
        "Rheumatology"],

    "Surgery & Cancer": [
        "Breast Surgery",
        "Colorectal Surgery",
        "ENT Surgery",
        "General Surgery",
        "Neurosurgery",
        "Orthopaedics"],

    "Women & Children": [
        "Gynaecology",
        "Obstetrics",
        "Paediatrics",
        "Postnatal Care"],

    "Emergency & Urgent Care": [
        "Emergency Department",
        "Urgent Care",
        "Ambulance Services",
        "Minor Injuries Unit"],

    "Critical Care & Anaesthesia": [
        "Intensive Care Unit",
        "Anaesthesia",
        "Pain Management"],

    "Clinical Support Services": [
        "Radiology",
        "Pathology",
        "Pharmacy",
        "Physiotherapy",
        "Occupational Therapy"],
    "Corporate Services": [
        "Human Resources",
        "Finance",
        "IT Support",
        "Facilities Management",
        "Communications"
    ]
}

bands = {
    "Healthcare Assistant": "2",
    "Nursery Nurse": "2",
    "Administrator": "3",
    "Receptionist": "3",
    "Medical Secretary": "4",
    "Staff Nurse": "5",
    "Pharmacist": "5",
    "Physiologist" : "6",
    "Physiotherapist": "6",
    "Occupational Therapist": "6",
    "Radiographer": "6",
    "Speech Therapist": "6",
    "Senior Staff Nurse": "6",
    "Charge Nurse": "7",
    "Ward Manager": "8A",
    "Data Analyst" : "8A",
    "FY1/FY2": "FY1",
    "SHO": "SHO",
    "Registrar": "SPR",
    "Consultant": "CONS",
    "GP" : "GP"
}

salary_range = {
    "2": (24000,28000),
    "3": (26000,32000),
    "4": (30000,38000),
    "5": (37000,45000),
    "6": (44000,55000),
    "7": (52000,65000),
    "8A": (55000,70000),
    "FY1": (36000,42000),
    "SHO": (45000,60000),
    "SPR": (65000,85000),
    "CONS": (95000,140000),
    "GP": (90000,120000)
}

ethnicities = {
    "White": ["United Kingdom", "United States", "Canada", "Australia", "New Zealand"],
    "Black": ["Nigeria", "Ghana", "Kenya", "South Africa","Jamaica", "Trinidad and Tobago", "Barbados"],
    "Asian": ["China", "Japan", "India", "Thailand"],
    "Mixed": ["United Kingdom", "United States", "Canada", "Australia", "New Zealand", "Nigeria", "Ghana", "Kenya", "South Africa", "China", "Japan", "India", "Thailand", "Jamaica", "Trinidad and Tobago", "Barbados"],

}
contract_types = [
    "Permanent",
    "Fixed Term",
    "Bank"
]

employment_status = [
    "Active",
    "On Leave",
    "Suspended",
    "Inactive"
]


visa_status = {
    "British Citizen": ["United Kingdom", "United States", "Canada", "Australia", "New Zealand", "Nigeria", "Ghana", "Kenya", "South Africa", "China", "Japan", "India", "Thailand", "Jamaica", "Trinidad and Tobago", "Barbados"],
    "ILR": ["United States", "Canada", "Australia", "New Zealand", "Nigeria", "Ghana", "Kenya", "South Africa", "China", "Japan", "India", "Thailand", "Jamaica", "Trinidad and Tobago", "Barbados"],
    "Skilled Worker": ["United States", "Canada", "Australia", "New Zealand", "Nigeria", "Ghana", "Kenya", "South Africa", "China", "Japan", "India", "Thailand", "Jamaica", "Trinidad and Tobago", "Barbados"],
    "Dependent": ["United States", "Canada", "Australia", "New Zealand", "Nigeria", "Ghana", "Kenya", "South Africa", "China", "Japan", "India", "Thailand", "Jamaica", "Trinidad and Tobago", "Barbados"]
}

registration_types = [
    "NMC",
    "HCPC",
    "GMC",
    "None"
]

# ------------------------------
# Generate Employee Data
# ------------------------------

rows = []

for emp in range(1, NUMBER_OF_EMPLOYEES+1):
    sg = random.choice(list(staff_groups.keys()))
    role = random.choice(staff_groups[sg])
    division = random.choice(list(divisions.keys()))
    ward = random.choice(divisions[division])
    grade = bands[role]
    salary = random.randint(
        salary_range[grade][0],
        salary_range[grade][1]
    )
    hire_date = faker.date_between(start_date='-10y', end_date='today')
    contract_start = hire_date + relativedelta(weeks=random.randint(4, 6))
    weekly_hours = random.choice([37.5, 30, 20, 15,18.75])
    fte = round(weekly_hours / 37.5, 2)
    ethnicity = random.choice(list(ethnicities.keys()))
    nationality = random.choice(ethnicities[ethnicity])
    visa = random.choice(list(visa_status.keys()))
    visa_country = random.choice(visa_status[visa])
    profile_date = hire_date + relativedelta(weeks=3)

    rows.append({
        "Employee ID": f"EMP{emp:04d}",
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "DOB": faker.date_of_birth(minimum_age=18, maximum_age=65),
        "Telephone": faker.phone_number(),
        "Address": faker.address(),
        "Gender": random.choice(["Male", "Female"]),
        "Trust": random.choice(trust_name),
        "Ethnicity": ethnicity,
        "Nationality": nationality,
        "Visa Status": visa,
        "Staff Group": sg,
        "Role": role,
        "Division": division,
        "Ward": ward,
        "Grade": grade,
        "Salary": salary,
        "Hire Date": hire_date,
        "Contract Start": contract_start,
        "Weekly Hours": weekly_hours,
        "FTE": fte,
        "Registration Type": random.choice(registration_types),
        "Contract Type": random.choice(contract_types),
        "Employment Status": random.choice(employment_status),
        "Registration Number": faker.bothify(text='??######', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "NI Number": faker.bothify(text='??######', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "Registration Expiry Date": faker.date_between(start_date='today', end_date='+5y'),
        "DBS Expiry Date": faker.date_between(start_date='today', end_date='+5y'),
        "Mandatory Training Completion Date": faker.date_between(start_date='-1y', end_date='today'),
        "Mandatory Training Expiry Date": faker.date_between(start_date='today', end_date='+1y'),
        "Profile Date": profile_date
    })


def create_employee_data():
    """
    Create a pandas DataFrame from the generated employee data.
    """
    df = pd.DataFrame(rows)

    filename = f"employee_data_{filename_timestamp}.csv"

    print(f"\n Generated employee data for {len(rows)} employees and saved to {filename}")

    return df.to_csv(filename, index=False)