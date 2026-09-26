import pandas as pd

# Creating DataFrame for Student Detail
details = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'NAME': [
        'Jagroop', 'Praveen', 'Harjot', 'Pooja', 'Rahul',
        'Nikita', 'Saurabh', 'Ayush', 'Dolly', 'Mohit'
    ],
    'BRANCH': [
        'CSE', 'CSE', 'CSE', 'CSE', 'CSE',
        'CSE', 'CSE', 'CSE', 'CSE', 'CSE'
    ]
})

# Creating DataFrame for Fees Status
fees_status = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'PENDING': [
        '5000', '250', 'NIL', '9000', '15000',
        'NIL', '4500', '1800', '250', 'NIL'
    ]
})

# Printing Student Details
print("Student Details:")
print(details)

# Printing Fees Status
print("\nFees Status:")
print(fees_status)

# Merging the two DataFrames using ID
result = pd.merge(details, fees_status, on='ID')

# Printing the merged DataFrame
print("\nMerged Student Details and Fees Status:")
print(result)