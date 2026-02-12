import json
import os

def process_query(query):
    query = query.lower()

    # Get absolute path safely
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "..", "data", "admissions_data.json")
    data_path = os.path.abspath(data_path)

    try:
        with open(data_path, "r") as file:
            data = json.load(file)
    except Exception as e:
        return f"Error loading data file: {str(e)}"

    for course in data:
        if course.lower() in query:
            course_data = data[course]

            if "eligibility" in query:
                return f"{course} Eligibility: {course_data['eligibility']}"

            elif "start" in query or "admission" in query:
                return f"{course} Admission Info: {course_data['admission_start']}"

            elif "document" in query:
                docs = ", ".join(course_data["documents"])
                return f"{course} Required Documents: {docs}"

            else:
                return f"{course} Details: Eligibility - {course_data['eligibility']}, Admission Start - {course_data['admission_start']}"

    return "Sorry, I couldn't find information for that course."