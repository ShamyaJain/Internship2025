import requests
import json
import pandas as pd

API_URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"
OUTPUT_FILE = "employees_cleaned.csv"

def fetch_employee_data(api_url):
    """Fetch employee data from the API and return it as JSON."""
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()  # Get the full JSON response

        # Debugging: Print first few entries to check structure
        if isinstance(data, list):
            print("API returned a list, using it directly.")
            return data  # Directly return the list of employees
        elif isinstance(data, dict) and "employees" in data:
            print("API returned a dictionary, extracting 'employees'.")
            return data["employees"]
        else:
            print("Unexpected data format:", data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def clean_phone_number(phone):
    """Clean phone numbers and mark invalid ones."""
    if 'x' in phone or not phone.replace('-', '').replace('.', '').isdigit():
        return "Invalid Number"
    return int(''.join(filter(str.isdigit, phone)))

def get_designation(years_of_experience):
    """Determine employee designation based on experience."""
    if years_of_experience < 3:
        return "System Engineer"
    elif 3 <= years_of_experience <= 5:
        return "Data Engineer"
    elif 5 < years_of_experience <= 10:
        return "Senior Data Engineer"
    return "Lead"

def process_employee_data(data):
    """Process raw employee data into a structured DataFrame."""
    processed_data = []
    for emp in data:
        try:
            processed_data.append({
                "Full Name": f"{emp['first_name']} {emp['last_name']}",
                "email": emp["email"],
                "phone": clean_phone_number(emp["phone"]),
                "gender": emp["gender"],
                "age": int(emp["age"]),
                "job_title": emp["job_title"],
                "years_of_experience": int(emp["years_of_experience"]),
                "salary": int(emp["salary"]),
                "department": emp["department"],
                "designation": get_designation(int(emp["years_of_experience"]))
            })
        except KeyError as e:
            print(f"Missing key {e} in record {emp}. Skipping entry.")
        except ValueError as e:
            print(f"Invalid value encountered: {e}. Skipping entry.")
    
    return pd.DataFrame(processed_data)

if __name__ == "__main__":
    raw_data = fetch_employee_data(API_URL)
    if raw_data:
        df = process_employee_data(raw_data)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"Processed data saved to {OUTPUT_FILE}")