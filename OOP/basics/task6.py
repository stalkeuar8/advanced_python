import bcrypt
import zxcvbn

class SecurePassword:
    def __init__(self, hashed_password):
        self.password = hashed_password

    @property
    def password(self):
        raise PermissionError("Password cant be shown.")
    
    @password.setter
    def password(self, raw_password):
        if len(raw_password) < 8:
            raise ValueError("Password must be longer than 8.")
        if not any(c.islower() for c in raw_password):
            raise ValueError("Password must contain lowercase letter.")
        if not any(c.isupper() for c in raw_password):
            raise ValueError("Password must contain uppercase letter.")
        if not any(c.isdigit() for c in raw_password):
            raise ValueError("Password must contain digit.")
        if self.strength(raw_password)[0] != 0 and self.strength(raw_password)[0] != 1:
            password = raw_password.encode("utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            self._password = hashed_password
        else:
            raise ValueError("Password is to week!")


    def strength(self, password):
        metrics = {0:"Very Week", 1: 'Week', 2: "Medium", 3: "Strong", 4: "Best"}
        res = zxcvbn.zxcvbn(password)
        if res['score'] in metrics.keys():
            return [res['score'], metrics[res["score"]]]
        else:
            raise KeyError("Not found metrics.")


    def verify_pass(self, password_to_check):
        encoded_pass_to_check = password_to_check.encode('utf-8')
        return bcrypt.checkpw(encoded_pass_to_check, self._password)
          
    

try:
    user_pass = SecurePassword('1qweRTY22X')
    res = user_pass.verify_pass('1qweRTY22X')
    print(res)
    

except Exception as e:
    print(e)
    