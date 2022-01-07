letter = ''' name \n
you are selected \n
join our company on \n
date 
'''
a = input("enter the name ")
b = input("enter the date ")
print(letter.replace("name",a))
print(letter.replace("date",b))