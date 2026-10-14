1. PURPOSE
- Manage employees in JSON file and make operations on it.
- Create virtual env and install dependencies like rich.
- Create different branches for features and merge them in main.
- Create requirements.txt and .gitignore

2. Setup:
- create virtual env (python -m venv .venv)
- Activate it (.venv/Scripts/ativate)
- Run: python -m empmgr.cli (from root)


3. Structure:
>> git status
*   1358412 (HEAD -> main) Merge department report
|\  
| * 730e9a0 (feature/report) Export department report functionality
| * f6028c9 Add department summary report
* |   32f0ce1 Merge validation feature
|\ \  
| |/  
|/|   
| * 2776754 (feature/validation) Add email validation
|/  
* 1daab0e Add project dependencies
* 367e34b Add sample employee records
* c5e28f2 Add employee management cli file
* bf5887f Add employee management cli file
* 4f3d43a Add salary input validation
* 53525f4 Add employee JSON file storage
* 54a8767 Add employee model to add employee
On branch main
nothing to commit, working tree clean