#! /bin/bash

echo "Pipeline started at: $(date)"

# =====================================================================
# NHS Workforce - Data Ingestion Pipeline
# =====================================================================
#
# This script performs a simple extract and load porcess:
#
#  1. File Generation:
#     Data is generated using python libraries like random & Faker.
#     The generated data is stored as a CSV file and moved into the 
#     raw folder.
#
#  2. Load:
#     The generated data is then loaded into the database created using
#     PostgreSQL
# =====================================================================


# -----------------------------------------------------------------------
# STEP 1: Set base directory
# -----------------------------------------------------------------------

LOGFILE=~/my_projects/healthcare_workforce_project

echo "Current directory: ${LOGFILE}"
echo ""

# -----------------------------------------------------------------------
# STEP 2: Run main.py to generate datasets
# -----------------------------------------------------------------------
echo "Generating employees and vacancies datasets"
echo ""

if python3 "${LOGFILE}/python_scripts/main.py"; then
    echo "Data generation completed"
    echo ""
else
    echo "ERROR: Failed to complete data generation"
    exit 1
fi

# -----------------------------------------------------------------------
# STEP 3: Move generated data into raw folder
# -----------------------------------------------------------------------
echo ""
echo "Moving generated datasets into the raw folder"
echo ""

mv "${LOGFILE}"/*.csv "${LOGFILE}/raw"

echo "Data moved successfully to raw folder"
echo ""

# -----------------------------------------------------------------------
# STEP 4: Load data into PostgreSQL
# -----------------------------------------------------------------------
echo "Loading CSV files into the database"
echo ""

if python3 "${LOGFILE}/python_scripts/load.py"; then
    echo "Data loaded into the database"
else
    echo "ERROR: Failed to load data into the database"
    exit 1
fi

echo "============================================================"
echo "DATA PIPELINE COMPLETED SUCCESSFULLY"
echo "============================================================"

echo "Pipeline completed at: $(date)"
echo ""


