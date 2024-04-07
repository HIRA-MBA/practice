# Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your 
# prediction for the results of each test. 

carz = "honda"
print("Is carz == 'subaru'? I predict True.")
print(carz == 'honda') # true
print(carz =='Honda') # // false case sensitive

book1 = "harry potter"
print("Is book1 == 'harry potter'? I predict True.")
print(book1 == 'harry potter')# // true
print(book1 =='Harry Potter') # // false case sensitive

color = "green"
print("Is color == 'green'? I predict True.")
print(color == 'green') # // true
print(color =='red') # // false color changed

music = "jazz"
print("Is music == 'jazz'? I predict True.")
print(music == 'jazz') # // true
print(music =='jazz 2') # // false change jazz into jazz 2

animal = "Lion"
print("Is animal == 'Lion'? I predict True.")
print(animal == 'lion')#  // false case sensitive
print(animal =='Lion') # // true