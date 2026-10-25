numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

friends = ["Tom", "Tim", "Trent", "Bob", "Stacey"]
starts_t = [friend for friend in friends if friend.startswith("T")]
    
print(starts_t)

