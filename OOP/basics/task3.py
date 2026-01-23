import re

class User:
    def __init__(self, age, email):
        self.age = age
        self.email = email
        print(f"Age has been set successfully: {age}")
        print(f"Email has been set successfully: {email}")


    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email_text):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email_text):
            self._email = email_text
        else:
            raise ValueError("Email does not match correct format.")
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if 0 < value < 14:
            raise ValueError("User must be elder than 14.")
        elif value < 0:
            raise ValueError("Age must be positive and bigger than 14.")
        self._age = value
        

    def __str__(self):
        return f"User email: '{self._email}'\nUser age: {self._age}"

    @property
    def is_adult(self):
        if self._age > 30:
            return True
        else:
            return False
        
try:

    user = User(35, "myemail@gmail.com")
    print("\n")
    print(user)
    print("\n")
    print(user.is_adult)
except Exception as e:
    print(e)