from scrape import fetch_employee_data

def test_download():
    data = fetch_employee_data("https://api.slingacademy.com/v1/sample-data/files/employees.json")
    assert data is not None, "Failed to download data"
    print("Test Case 1: ✅ JSON file download successful")

test_download()
def test_extraction():
    data = fetch_employee_data("https://api.slingacademy.com/v1/sample-data/files/employees.json")
    assert isinstance(data, list), "Data is not a list"
    assert isinstance(data[0], dict), "Data entries are not dictionaries"
    print("Test Case 2: ✅ JSON file extraction successful")

test_extraction()
import os
import pandas as pd

def test_file_format():
    file_path = "employees_cleaned.csv"
    assert os.path.exists(file_path), "CSV file not created"
    df = pd.read_csv(file_path)
    assert not df.empty, "CSV file is empty"
    print("Test Case 3: ✅ CSV file created and valid")

test_file_format()
def test_data_structure():
    df = pd.read_csv("employees_cleaned.csv")
    expected_columns = [
        "Full Name", "email", "phone", "gender", "age",
        "job_title", "years_of_experience", "salary", "department", "designation"
    ]
    assert list(df.columns) == expected_columns, "Columns do not match expected structure"
    print("Test Case 4: ✅ Data structure is correct")

test_data_structure()
from scrape import process_employee_data

def test_invalid_data():
    invalid_data = [
        {
            "first_name": "John", 
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "phone": "123-456x7890",  # Invalid phone number
            "gender": "male",
            "age": 25,
            "job_title": "Engineer",
            "years_of_experience": 5,
            "salary": 10000,
            "department": "IT"
        }
    ]
    df = process_employee_data(invalid_data)
    assert df.iloc[0]["phone"] == "Invalid Number", "Invalid phone not handled"
    print("Test Case 5: ✅ Invalid data handled correctly")

test_invalid_data()