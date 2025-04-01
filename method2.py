from datetime import date
#Method types in class/OOP

class User:
    def _init_(self,username,age=None,is_admin=False):
        self.username = username
        self.is_admin = is_admin

    
    #1.instance method
    def get_username(self):
        return self.username
    
    #2.class method
    @classmethod #decorator
    def create_admin(cls,username):
        return cls(username,is_admin=True)
    
    @classmethod
    def user_with_age(cls,username,dob:int):
        current_year = date.today().year
        age = current_year - dob
        return cls(username,age)
    
    @staticmethod
    def add_email(username,email):
        return f"{username} has email {email}"
        
user1 = User("Ben")
# print(f"{user1.get_username()} is_admin:{user1.is_admin}")
user2 = User.create_admin("Kipngeno")
# print(f"{user2.get_username()} is_admin:{user2.is_admin}")
user3 = User.user_with_age("Doro",2000)
# print(f"{user3.get_username()} is_admin{user3.is_admin} age{user3.age}")
user4 = User.add_email("rop","rop@email.com")
print(user4)