class User:
    name = 'No name provided'
    email = ' '
    password = '123'
    account_number = 0
class Employee(User):
    base_pay = 15.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True

if __name__ == "__main__": 
    #Outside of the class you would create an instance of the User class
    new_user = User()
    print(new_user.password)
    new_employee = Employee()
    print(new_employee.department)
    
