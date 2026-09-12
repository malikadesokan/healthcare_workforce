#! /bin/bash

# Set base directory

LOGFILE=~/my_projects/healthcare_workforce_project

echo "Current directory: ${LOGFILE}"

# Run Python script to generate employee datasets
python3 "${LOGFILE}/python_scripts/main.py" 

# Move the generated data into the raw folder
mv "${LOGFILE}"/*.csv "${LOGFILE}/raw"

echo "Data moved Successfully"
