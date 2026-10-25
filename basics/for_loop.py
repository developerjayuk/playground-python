friends = [("Bob", 12), ("Steve", 53), ("Jane", 34)]
total = 0

for friend in friends:
  print(f"{friend[0]} is one of the friends.")
  total+= int(friend[1])

print(f"Average age of the friends is {total / len(friends)}" )
  