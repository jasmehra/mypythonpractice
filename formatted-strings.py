name = "Jasleen"
age=22
print("Hi "+name+". You are "+str(age)+" years old !")

print(f"Hii {name}. You are {age} years old !")

print("Hii {0}. You are {1} years old !".format(name,age))

print("Hii {1}. You are {0} years old !".format(name,age))

print("Hii {}. You are {} years old !".format(name,age))

#print("Hii {}. You are {} years old !".format(new_name='abcd',new_age=32))   #error tuple out of range

print("Hii {new_name}. You are {new_age} years old !".format(new_name='abcd',new_age=32)) 
