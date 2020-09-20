import re


class BasePasswordManager:

    def old_passwords(self):
        old_pass = ['247abc', 'abc247', '247365bac', '247365bac$']
        self.old_pass = old_pass[-1]
        return self.old_pass

    def get_password(self):
        current_pass = self.old_pass
        self.current_pass = current_pass
        return "Current password is " + self.current_pass

    def is_correct(self, pwd=input('enter your password: ')):
        self.pwd = pwd
        print("New password is the same as the current password:", self.pwd == self.current_pass)
        return self.pwd


class PasswordManager(BasePasswordManager):

    def get_level(self):
        self.security_lvl = 0
        check_al = False
        check_num = False
        if self.pwd.isdigit():
            self.security_lvl = 0
            print('Security level', self.security_lvl, ':WEAK')
            print('Password consists of digits only')
        elif self.pwd.isalpha():
            self.security_lvl = 0
            print('Security level', self.security_lvl, ':WEAK')
            print('Password consists of alphabets only')
        elif check_al == False and check_num == False and (bool(re.match('^[a-zA-Z0-9]*$', self.pwd)) == True):
            for i in self.pwd:
                if i.isalpha():
                    check_al = True
            for j in self.pwd:
                if j.isnumeric():
                    check_num = True
            if check_al == True and check_num == True:
                self.security_lvl = 1
                print('Security level', self.security_lvl, ':  MODERATE')
                print('Password is alphanumeric with NO special characters')
        elif check_al == False and check_num == False:
            for i in self.pwd:
                if i.isalpha():
                    check_al = True
            for j in self.pwd:
                if j.isnumeric():
                    check_num = True
            if check_al == True and check_num == True and (bool(re.match('^[a-zA-Z0-9]*$', self.pwd)) == False):
                self.security_lvl = 2
                print('Security level', self.security_lvl, ':STRONG')
                print('Password is alphanumeric with special characters')
            else:
                self.security_lvl = 1
                print('Security level', self.security_lvl, ':  MODERATE')
                print('Password contains special characters with either numbers or alphabets only')

    def set_password(self):
        if len(self.pwd) < 6:
            print("New password must have 6 characters or more")
            print("Password change:UNSUCCESSFUL")
        elif self.security_lvl < 2:
            print("New password must contain at least 1 special character with numbers and alphabets")
            print("Password change:UNSUCCESSFUL")
        elif self.pwd == self.current_pass:
            print("Password change: No changes detected")
        else:
            print("Password change:SUCCESSFUL")


current = PasswordManager()

current.old_passwords()
current.get_password()
current.is_correct()
current.get_level()
current.set_password()
