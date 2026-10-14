from rich.console import Console
from rich.table import Table

from .models import add_employee
from .storage import load_employees, save_employees
from .validators import parse_salary , is_valid_email
console = Console()



def show_employees() -> None:
    """Display employees in a Rich table."""
    table = Table(title="Employees")

    for column in ("ID", "Name", "Department", "Salary"):
        table.add_column(column)

    for emp in load_employees():
        table.add_row(
            str(emp["id"]),
            emp["name"],
            emp["department"].strip().lower(),
            f"{emp['salary']:,.2f}",
        )

    console.print(table)


def main() -> None:
    while True:
        print("\n=== Employee Manager ===")
        print("1. List employees")
        print("2. Add employee")
        print("3. Department report")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_employees()

        elif choice == "2":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            department = input("Department: ").strip()
            salary = parse_salary(input("Salary: ").strip())

            if not name or not department:
                print("Name and department are required.")
                continue

            if not is_valid_email(email):
                print("Invalid email address.")
                continue

            if salary is None:
                print("Enter a valid non-negative salary.")
                continue

            employees = load_employees()
            add_employee(employees, name, email, department, salary)
            save_employees(employees)
            print("Employee added successfully.")

        elif choice == "3":
            from .report import department_summary

            summary = department_summary()
            table = Table(title="Department Summary")
            table.add_column("Department")
            table.add_column("Headcount", justify="right")
            table.add_column("Average Salary", justify="right")

            for department, values in sorted(summary.items()):
                table.add_row(
                    department,
                    str(values["headcount"]),
                    f"{values['average_salary']:,.2f}",
                )

            console.print(table)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()