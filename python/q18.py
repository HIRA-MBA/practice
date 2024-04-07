#  18 array of cities in order
cities  = ["Islamabad","Quetta","Lahore","Sialkot","Multan"]
print("original cities : ", cities)
print("cities in alphabatic order without modifying :", sorted(cities))
print("original cities : ", cities)
print("cities in reverse alphabatic order without modifying : " ,sorted(cities,reverse='true'))
print("original cities : ", cities)

# • Reverse the order of your list. Print the array to show that its order has changed.

cities.sort(reverse='true')
print("cities in reverse alphabatic order : ",cities)

# • Reverse the order of your list again. Print the list to show it’s back to its original order.
cities.reverse()
print("cities in reverse alphabatic order : " ,cities)
#• Sort your array so it’s stored in alphabetical order.
#  Print the array to show that its order has been changed.
cities.sort()
print("cities in alphabatic order : ",cities)

#• Sort to change your array so it’s stored in reverse alphabetical order.
#  Print the list to show that its order has changed.
cities.reverse()
print("cities in reverse alphabatic order : " ,cities)