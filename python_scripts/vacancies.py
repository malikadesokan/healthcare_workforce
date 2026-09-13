import random
import pandas as pd
from faker import Faker
from datetime import datetime, time, timedelta, date
from dateutil.relativedelta import relativedelta
from variable import trust_name
from employees import staff_groups, divisions, bands, rate_range, NUMBER_OF_EMPLOYEES

faker = Faker("en_GB")

filename_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
batch_timestamp = datetime.now().date().strftime("%Y%m%d")

NUMBER_OF_VACANCIES = 10000

employee_id = []

for emp in range(1, NUMBER_OF_EMPLOYEES +1):
        assignment_no = f"EMP{emp:04d}-{filename_timestamp}"
        employee_id.append(assignment_no)

request_reasons = [
    "Annual Leave Cover",
    "Sickness Cover",
    "Staff Shortage",
    "Increased Patient Demand",
    "Unexpected Absence",
    "Ward Capacity Increase",
    "Emergency Cover",
    "Specialist Skills Required",
    "Night Shift Cover",
    "Weekend Cover",
    "Bank Holiday Cover",
    "Maternity Leave Cover",
    "Training Cover",
    "Study Leave Cover",
    "Planned Leave Cover",
    "Staff Redeployment",
    "New Service Requirement",
    "High Acuity Patients",
    "Additional Patient Safety Cover",
    "Operational Requirement"
]

# ------------------------------
# Generate Employee Data
# ------------------------------

rows = []

for shift in range(1, NUMBER_OF_VACANCIES +1):
    # start_date = date.today() - relativedelta(month=7)
    # end_date = date.today() + relativedelta(month=2)

    shift_date = faker.date_between(start_date='-1y',end_date='+1y')
    shift_time = time(hour=random.randint(0,23),
                            minute=random.choice([0,15,30,45]))
    shift_datetime = datetime.combine(shift_date, shift_time)
    end_datetime = shift_datetime + timedelta(
                    hours=random.randint(1, 12))
    sg = random.choice(list(staff_groups.keys()))
    role = random.choice(list(staff_groups[sg]))
    division = random.choice(list(divisions.keys()))
    ward = random.choice(list(divisions[division]))
    request_grade = random.choice(list(staff_groups[sg]))
    booked_grade = random.choice(list(staff_groups[sg]))
    band = bands[booked_grade]
    day_rate = rate_range[band][0]
    night_rate = rate_range[band][1]
    
  
 
    rows.append({
        "booking reference": f"BR-{shift:08d}-{filename_timestamp}",
        "shift_date": shift_date,
        "start": shift_time,
        "end": end_datetime.time(),
        "trust": random.choice(trust_name),
        "staff group": sg,
        "ward": ward,
        "division": division,
        "request grade":request_grade,
        "booked grade": booked_grade,
        "payband": band,
        "day rate": day_rate,
        "night rate": night_rate,
        "staff_id" : random.choice(employee_id),
        "requester" : faker.name(),
        "request_reason" : random.choice(request_reasons),
        "booked date" : faker.date_between(start_date="-2y", end_date="today")

    })



def create_shift_data():
    """
    Create a pandas DataFrame from the generated employee data.
    """
    df = pd.DataFrame(rows)

    filename = f"shift_data_{filename_timestamp}.csv"

    print(f"\n Generated shift data for {len(rows)} shifts and saved to {filename}")

    return df.to_csv(filename, index=False)




