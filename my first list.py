'''
name = ['james', 'collins', 'juana']
password= ['doja', 'yoshi']
namee= input('name: ')
passwordd= input("password: ")
if namee in name and  passwordd in password:
    print('login successful')
else:
    print("invalid credentials")

'''
    


'''
name= []
password= []
hobbies= []

namee= int(input('how many names would you like to input'))
n= 0
while n< namee:
    name.append(n)
    n+=1
print (name)
'''



Name= input("what is your name")
Mobile= int(input("phone number"))
hbby= input("hobbies")
user= {"name" : Name, "number": Mobile, "hobbies": hbby}
print(user)


