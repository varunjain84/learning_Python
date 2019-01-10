friends = ["Abhay","Schubert","Tarang","Siddharth"]
friends2 = friends.copy()
print(friends2.reverse())
number= [2,4,6,8,0]
friends.sort()
print(friends)
print(friends[1],friends[2])
friends[3]="Jason"
print("He is my best mate " + friends[0])
print(friends[3])
print(number)
print(number[2])
friends.extend(number)
friends.append("Kaboom")
friends.insert(1,"Pokemon")
print(friends)