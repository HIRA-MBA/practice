#// // condtions true and one False result for each of the following:
#// // condtions true and one False result for each of the following:
#// • Tests for equality and inequality with strings
myCar= "honda"
print(" \n \t question 24 a \n ")
print( myCar == "honda")#// true
print( myCar != "honda")#// false
print( myCar != "Honda") #// true

#// • Tests using the lower case function

print(" \n \t question 24 b \n ")
print("Apple".lower()=="apple")#//true


#// • Numerical tests involving equality and inequality, greater than and less than, 
#// greater than or equal to, and less than or equal to
result  =75
print(" \n \t question 24 c \n ")
print( "result ===100" ,result ==100)#//false
print("result !=100" ,result !=100)#//true
print("result > 100" ,result > 100)#// false
print("result >= 100 " ,result >=100)#//false
print("result < 100" ,result < 100)#//true
print("result <= 100", result <= 100)#//true




# // • Tests using "and" and "or" operators
mynumber =10
print(" \n \t question 24 d \n ")
print( " mynumber > 2 and mynumber <20 " , mynumber > 2 and mynumber <20) #// true
print( " mynumber > 15 and mynumber <20 " , mynumber > 15 and mynumber <20)# // false
print( " mynumber > 2 or mynumber <20 " , mynumber > 2 or mynumber <20) #// true
print( " mynumber > 11 or mynumber <20 " , mynumber > 2 or mynumber <20)# // true

#// • Test whether an item is in an array
pets  = ["parrot","cat","duck"]
print(" \n \t question 24 e \n ")
if "cat" in pets :
 print(' pets includes "cat" ')
#// • Test whether an item is not in an array
print(" \n \t question 24 f \n ")
if "dog" not in pets :
    print(f' dog is not in pets')