myList = ["Jason", "Tom", "Dave"]
myTuple = ("Jason", "Tom", "Dave")
mySet = {"Jason", "Tom", "Dave"}
mySet2 = {"Tom", "Dave", "Sam"}

myList.append("Sara")
myList.remove("Jason")

print(myList[2])

mySet.add("Tom")
print(f"my final set: {mySet}")

diff = mySet.difference(mySet2)
print(diff)

total = mySet.union(mySet2)
print(total)

inter = mySet.intersection(mySet2)
print(inter)