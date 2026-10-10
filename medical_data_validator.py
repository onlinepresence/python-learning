import re

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list) and all([isinstance(med, str) for med in medications]),
        'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }

    return [key for key, val in constraints.items() if not val]

def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print("Data should be a list or tuple")
        return False

    is_invalid = False

    # create a set of the keys
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    # loop through and validate
    for index, dictionary in enumerate(data):
        # ensure the dictionary is indeed a dict
        if(not isinstance(dictionary, dict)):
            is_invalid = True
            print("Invalid object found in data at index", index)
            continue

        # check if the dictionary keys match
        if set(dictionary.keys()) != key_set:
            print("Invalid keys found at", index)
            is_invalid = True
            continue

        invalid_keys = find_invalid_records(**dictionary)

        if invalid_keys:
            is_invalid = True
            
            for key in invalid_keys:
                print(f"Invalid value found for '{key}: {dictionary.get(key)}' at index {index}")

        if(is_invalid):
            print("")

    if(is_invalid):
        return False
    
    print("Data is valid")
    return True

# test the validator
validate(medical_records)