

def pass_validator(password):
    if len(password) < 8:
        return False, "Password to short"
    if not any(c.isalpha() for c in password):
        return False, "Password must contain letter"
    if not any(c.isupper() for c in password):
        return False, "Password must contain uppercase letter"
    if not any(c.islower() for c in password):
        return False, "Password must contain lowercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain digit"
    if any(c == ' ' for c in password):
        return False, "Password must be without spaces"
    spec_symb = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in spec_symb for c in password):
        return False, "Password must contain special symbols"
    return True, "Password is valid"