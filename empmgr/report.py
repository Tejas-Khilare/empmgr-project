from .storage import load_employees


def department_summary():
    employees = load_employees()
    summary = {}

    for employee in employees:
        department = employee["department"].strip().lower()
        if department not in summary:
            summary[department] = {
                "headcount": 0,
                "total_salary": 0
            }

        summary[department]["headcount"] += 1
        summary[department]["total_salary"] += employee["salary"]

    report = {}

    for department, values in summary.items():
        report[department] = {
            "headcount": values["headcount"],
            "average_salary": (
                values["total_salary"] / values["headcount"]
            )
        }

    return report