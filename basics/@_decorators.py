import functools

user = {"username": "jose", "access_level": "admin"}


def admin_access(func):
    # @functools.wraps(func)
    def admin_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return admin_function


@admin_access
def get_admin_password():
    return "admin-0123"


print(get_admin_password())
print(get_admin_password.__name__)
