

# 15• Start with your program from Exercise 14. Add a print statement at the end of your program stating the
#  name of the guest who can’t make it.

guests_new  = ["sara","fara","maria"]
print("\n \t Assignment 15 \n")

print(f'{guests_new[0]} : i am glad to invite you on dinner this Sunday.')
print(f'{guests_new[1]} : i am glad to invite you on dinner this Sunday.')
print(f'{guests_new[2]} : i am glad to invite you on dinner this Sunday.')
guest_remove= guests_new.pop()
print(guests_new)
print(f'{guest_remove} is not coming on dinner so we are inviting new frind Marry')
guests_new.append("marry")
print(guests_new)
print(f'{guests_new[0]} : i am glad to invite you on dinner this Sunday.')
print(f'{guests_new[1]} : i am glad to invite you on dinner this Sunday.')
print(f'{guests_new[2]} : i am glad to invite you on dinner this Sunday.')

 # 16:add three more guest 
print("\n \t Assignment 16 \n")

guests_new.insert(0,"peter")
guests_new.insert(3,"Robert")
guests_new.append("Eric")
print(guests_new)
for guests_new in guests_new:
 print(f' {guests_new },you are invited on dinner this Sunday') 

 