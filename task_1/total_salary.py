
def total_salary(path):
    total_salary = 0
    count = 0

    with open(path, "r") as file:
        for line in file:
            try:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue
                total_salary +=  float(parts[1])
                count += 1
            except ValueError:
                continue

    average_salary = total_salary / count if count > 0 else 0

    return total_salary, average_salary
