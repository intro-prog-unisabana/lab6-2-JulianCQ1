def employee_print(employee_info):
    name = employee_info.get("nombre","N/A")
    salary = employee_info.get("salario","N/A")
    role = employee_info.get("rol","N/A")
    print(f"Name: {name}\nSalary: {salary}\nRole: {role}\n")
    remaining = employee_info.copy()
    remaining.pop("nombre", None)
    remaining.pop("salario", None)
    remaining.pop("rol", None)
    if remaining:
        for key, value in remaining.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")
