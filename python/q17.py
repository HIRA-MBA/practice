#17:shrinking guest list until 2 left
new_guests = ["peter","perker","robbert","sara","Mary","fara"]

print(" \n\t second approach for assignment 17 \n")

while  len(new_guests) > 2:
 removed_guest1= new_guests.pop()
 print(f"{removed_guest1},i can't you on dinner")
print(new_guests)
print(f'{new_guests[0]} you are still invited')
print(f'{new_guests[1]} you are still invited')
while  len(new_guests) > 0:
 new_guests.pop()

print(f"list is empty{ new_guests}")


