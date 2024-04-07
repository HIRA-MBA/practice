# 21.	They think of something you could store in a TypeScript Object.
#  Write a program that creates Objects containing these items.

book={'author':'Jane Austen',
'title':'Pride and Prejudice','yearPublish': 1813 }
print("\n \t assignment number 21 \n")

print(f" I like the book {book['title']} by {book['author']}  published in {book['yearPublish']} very much.")

fav_car={'manufacturer':'HONDA', 'make':'city ', 'model':2022}
print(f" I like the  {fav_car['make']} by ${fav_car['manufacturer']} model {fav_car['model']} very much.")

# 22.	Intentional Error: If you haven’t received an array index error in one of your programs yet,
# try to make one happen. Change an index in one of your programs to produce an index error.
# Make sure you correct the error before closing the program.
print("\n \t assignment number 22 \n")
abc  =["a","b","c","d"]
#print(abc[5])# index 5 undefined
print(abc[3])