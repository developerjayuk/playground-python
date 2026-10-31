def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Teddy Jones", "age": 98},
    {"name": "Adam Smith", "age": 56},
    {"name": "Sarah Jane", "age": 21},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Adam Smith", get_friend_name))
