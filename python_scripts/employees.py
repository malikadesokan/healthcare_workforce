import random
import pandas as pd
from faker import Faker
from datetime import datetime
from dateutil.relativedelta import relativedelta
from variable import trust_name

faker = Faker("en_GB")

filename_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
batch_timestamp = datetime.now().date().strftime("%Y%m%d")

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

rate_range = {
    "2": (12.31, 14.36),
    "3": (13.33, 16.41),
    "4": (15.38, 19.49),
    "5": (18.97, 23.08),
    "6": (22.56, 28.21),
    "7": (26.67, 33.33),
    "8A": (28.21, 35.90),
    "FY1": (18.46, 21.54),
    "SHO": (23.08, 30.77),
    "SPR": (33.33, 43.59),
    "CONS": (48.72, 71.79),
    "GP": (46.15, 61.54)
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
    rate = random.uniform(
        rate_range[grade][0],
        rate_range[grade][1]
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
        "emp_id" : f"EMP{emp:04d}-{filename_timestamp}",
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "dob": faker.date_of_birth(minimum_age=18, maximum_age=65),
        "telephone": faker.phone_number(),
        "address": faker.address(),
        "gender": random.choice(["Male", "Female"]),
        "trust": random.choice(trust_name),
        "ethnicity": ethnicity,
        "nationality": nationality,
        "visa_status": visa,
        "staff_group": sg,
        "role": role,
        "division": division,
        "grade": grade,
        "hourly_rate": round(rate,2),
        "hire_date": hire_date,
        "contract_start": contract_start,
        "weekly_hours": weekly_hours,
        "fte": fte,
        "registration_type": random.choice(registration_types),
        "contract_type": random.choice(contract_types),
        "employment_status": random.choice(employment_status),
        "registration_no": faker.bothify(text='??######', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "registration_expiry_date": faker.date_between(start_date='today', end_date='+5y'),
        "ni": faker.bothify(text='??######', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "dbs_expiry_date": faker.date_between(start_date='today', end_date='+5y'),
        "mandatory_training_expiry_date": faker.date_between(start_date='today', end_date='+1y'),
        "profile_creation_date": profile_date
    })


def create_employee_data():
    """
    Create a pandas DataFrame from the generated employee data.
    """
    df = pd.DataFrame(rows)

    filename = f"employee_data_{filename_timestamp}.csv"

    print(f"\n Generated employee data for {len(rows)} employees and saved to {filename}")

    return df.to_csv(filename, index=False)