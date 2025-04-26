employees = ["Mayank Sharma", "Mayank Sharma1", "Sumit Sharma", "Vinayak Kanchan"]

new_employee = ""

def add_unique(new_name):
    for name in employees:
        last_letter = name[-1]
        if ord(last_letter) >= 49 and ord(last_letter) <= 57:
            
            
            diff = ord(last_letter) - 49
            new_char = diff + 1
            new_employee = f"{new_name}{new_char}"
            employees.append(new_employee)
        else:
            