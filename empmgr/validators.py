
def parse_salary(text: str)->float | None:
    """Return a non-negative salary or None if invalid."""
    try:
        salary = float(text)
    except ValueError:
        return None
    if salary<0:
        return None
    return salary

def is_valid_email(email:str)->bool:
    """Check if email is valid or not..."""

    local_set={'+','-','.'}
    email.strip().lower()
    if email.count('@')<1 or email.count('@')>1:
        return False
    if " " in email or ".@" in email or "@." in email or ".@." in email or ".." in email:
        return False
    if email[0]=='.' or email[len(email)-1]=='.':
        return False
    local,domain=email.split('@')
    print(local)
    print(domain)
    for i in local:
        if i in local_set or (97<= ord(i) <=122) or (48<= ord(i) <=57):
            return True
        else:
            return False
    for j in domain:
            if j in local_set or (97<= ord(i) <=122) or  (48<= ord(i) <=57):
                return True
            else:
                return False
    return True


