import functools

user = {"username": "jose", "access_level": "admin"}


def admin_access(func):
    @functools.wraps(func)
    def admin_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return admin_function


@admin_access
def get_admin_password(panel):
    if panel == "admin":
        return "admin-0123"
    elif panel == "billing":
        return "billing-0123"

    return "admin-0123"


print(get_admin_password("admin"))
print(get_admin_password("billing"))
print(get_admin_password.__name__)
