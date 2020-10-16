# Python-PasswordManager
Note: This password manager was made as a project and is NOT intended for actual use.

Objective: To develop a custom password manager using Python

Domain:  Security

Steps to perform:            

Implement the following design
class BasePasswordManager

    members

        old_passwords: is a list that holds all of the user's past

                           passwords.

                           The last item of the list is the user's current password.

    methods

        get_password method that returns the current password as a string.

 

        is_correct method that receives a string and returns a boolean

             True or False depending on whether the string is equal to

             the current password or not.

 

class PasswordManager

    This class inherits from BasePasswordManager

 

        methods

        set_password method that sets the user's password.

             Password change is successful only if:

                    - Security level of the new password is greater.

                    - Length of new password is minimum 6

 

             However, if the old password already has the highest security level,

             new password must be of the highest security level for a successful password change.

 

        get_level method that returns the security level of the current password.

             It can also check and return the security level of a new password passed as a string.

 

Security levels:

         level 0 - password consists of alphabets or numbers only.

        level 1 - Alphanumeric passwords.

             level 2 - Alphanumeric passwords with special characters.
![PasswordManager](https://user-images.githubusercontent.com/68540614/96206683-c241b180-0f69-11eb-8ac1-0d996a8e15b2.gif)

