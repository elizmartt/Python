class AdministrativePrivileges:
    def __init__(self):
        pass

    def manage_users(self):
        return "Can manage users as an admin."


class User:
    def __init__(self, username):
        self.username = username

    def display_info(self):
        return f"User: {self.username} cant manage as an admin"


class Admin(User, AdministrativePrivileges):
    def __init__(self, username):
        User.__init__(self, username)
        AdministrativePrivileges.__init__(self)

    def display_info(self):
        return f"Admin: {self.username}"


def main():

    admin = Admin("elizmartt")
    print(admin.display_info())
    print(admin.manage_users())

    user = User("ajhfia")
    print(user.display_info())


if __name__ == "__main__":
    main()
