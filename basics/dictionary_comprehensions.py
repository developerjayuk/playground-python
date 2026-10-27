users = [
    (0, "Bobby", "bobby@example.com"),
    (1, "Sally", "sally@example.com"),
    (2, "Sam", "sam@example.com"),
    (3, "Dave", "dave@example.com")
]

username_mapping = {user[0]: user[2] for user in users}

print(username_mapping[0])  # Output: bobby@example.com