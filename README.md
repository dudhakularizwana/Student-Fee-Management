# Student Fee Management using Pandas

## Overview

This project demonstrates how to use **Python Pandas** to create, display, and merge student details with their fee payment status.

Two separate DataFrames are created:

- Student Details
- Fees Status

The two DataFrames are merged using the common **ID** column.

## Objectives

- Create DataFrames using Pandas.
- Store student information.
- Store student fee status.
- Display student details and fee information.
- Merge two DataFrames using a common ID.
- Understand basic Pandas DataFrame operations.

## Technologies Used

- Python
- Pandas

## DataFrames Used

### 1. Student Details

The Student Details DataFrame contains:

- ID
- NAME
- BRANCH

### 2. Fees Status

The Fees Status DataFrame contains:

- ID
- PENDING

The `PENDING` column stores the pending fee amount for each student.

## Data Processing

The project performs the following steps:

1. Import the Pandas library.
2. Create the Student Details DataFrame.
3. Create the Fees Status DataFrame.
4. Display both DataFrames.
5. Merge both DataFrames using the `ID` column.
6. Display the final merged DataFrame.

## Merge Operation

The two DataFrames are merged using:

```python
result = pd.merge(details, fees_status, on='ID')


The ID column is used as the common key between the two DataFrames.
How to Run

Step 1: Install Pandas
pip install pandas

Step 2: Run the Python program
python student_fees.py

Project Structure
Student-Fee-Manegment/
│
├── student_fees.py

OUTPUT:
The program displays:
1. Student Details
2. Fees Status
3. Merged Student Details and Fees Status
The final output combines student information with their pending fee status.

AUTHOR
Dudekula Rizwana

CONCLUSION:
This project provides a simple example of using Pandas DataFrames and the merge() function to combine related student and fee information.
It is useful for understanding basic data manipulation and DataFrame operations in Python.

Thank You
Thank you for visiting this project!
