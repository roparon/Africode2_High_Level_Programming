class User:
    def __init__(self, name,phone, is_admin, is_logged_in):
        self.name = name
        self.phone = phone
        self.is_admin = is_admin
        self.is_logged_in = is_logged_in
    def user_roles(self):
        if self.is_logged_in and self.is_admin:
            return "Dashboard"
        elif not self.is_logged_in:
            return "Login Page"
        else:
            return "News feed"
user1 = User("Ben", "0710160400", is_logged_in=True, is_admin=False)
user2 = User("Jane", "0712345678", is_logged_in=True, is_admin=True)

print(f"{user1.name} redirected to {user1.user_roles()}")
print(f"{user2.name} redirected to {user2.user_roles()}")