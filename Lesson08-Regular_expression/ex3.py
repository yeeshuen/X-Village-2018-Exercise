import re

class AuthSystem:
    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compile(r'Tommy7410')
        self.password_regex = re.compile(r'tom7410')
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username")
            return True
        else: 
            print("Wrong username")
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            print("Wrong password")
            return False
    
    def check_username_format(self,username):
        if 6<=len(username)<12:
            pattern=r"[A-Z][a-zA-z0-9]{5,10}"
            if re.search(pattern,username):
                return True
            else:
                print("Username format error!"\
                "Your username is {}".format(username))
                return False
        else:
            print("Username length error!"\
            "Your username length is {}".format(len(username)))
            return False
            
    
    def check_password_format(self,password):
        if len(password)>=6:
            pattern=r"[a-z0-9]+"
            if re.search(pattern,password):
                return True
            else:
                print("Password format error!"\
                "Your password is {}".format(password))
                return False
        else:
            print("Password length error!"\
            "Your password length is {}".format(len(password)))
            return False


        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self.check_username_format(username):
            return

        if not self.check_password_format(password):
            return

        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Valid user")
        print("Welcom, {}!".format(username))

    
# Construct a object of type AuthSystem
auth = AuthSystem()

username=input("Enter your username:")
password=input("Enter your password:")

# authenticate the user's credentials
auth.authenticate(username,password)